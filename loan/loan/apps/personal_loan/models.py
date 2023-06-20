from django.db import models
from apps.personal_loan.choices import FieldTypeChoices
import uuid

class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

# Create your models here.
class LoanFields(BaseModel):

    field_name = models.CharField(max_length=255, blank=False, unique=True)
    field_type = models.CharField(max_length=100, 
                                  choices=[(ft.value, ft.value) for ft in FieldTypeChoices])
    
class LoanProposal(BaseModel):
    pass

class LoanProposalField(BaseModel):

    #Not using loanfields as foreign key, so can delete a field and maintain old entries
    proposal = models.ForeignKey(LoanProposal, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255, blank=False, unique=True)
    field_type = models.CharField(max_length=100, 
                                  choices=[(ft.value, ft.value) for ft in FieldTypeChoices])
    data = models.CharField(max_length=255)