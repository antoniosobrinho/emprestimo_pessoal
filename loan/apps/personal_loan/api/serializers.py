from rest_framework.serializers import ModelSerializer
from apps.personal_loan.models import LoanProposal
from apps.personal_loan.choices import LoanStatusChoices
from apps.personal_loan.tasks import rating_loan

class LoanProposalSerializer(ModelSerializer):

    class Meta:
        model = LoanProposal
        fields = '__all__'
        read_only_fields = ['status']

    
    def create(self, validated_data):

        validated_data['status'] = LoanStatusChoices.PENDING.value

        instance = super().create(validated_data)

        rating_loan.delay(str(instance.id))

        return instance


    