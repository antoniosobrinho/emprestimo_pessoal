from rest_framework.serializers import ModelSerializer
from apps.personal_loan.models import LoanProposal
from apps.personal_loan.choices import LoanStatusChoices

class LoanProposalSerializer(ModelSerializer):

    class Meta:
        model = LoanProposal
        fields = '__all__'
        read_only_fields = ['status']

    
    def create(self, validated_data):

        validated_data['status'] = LoanStatusChoices.PENDING.value
        return super().create(validated_data)


    