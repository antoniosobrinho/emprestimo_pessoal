from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from apps.personal_loan.validators import numeric_validator
from apps.personal_loan.choices import LoanStatusChoices
import uuid

class LoanProposal(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    document_number = models.CharField(max_length=11, blank=False, 
                                       validators=[numeric_validator, MinLengthValidator(11)])
    address = models.CharField(max_length=255)
    loan_value = models.DecimalField(decimal_places=2, max_digits=10,
                                      validators=[MinValueValidator(0)])
    status = models.CharField(max_length=10, choices=[(ls.value, ls.value) for ls in LoanStatusChoices])