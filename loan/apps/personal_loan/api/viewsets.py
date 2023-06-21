from rest_framework import mixins, viewsets
from apps.personal_loan.models import LoanProposal
from apps.personal_loan.api.serializers import LoanProposalSerializer

class LoanProposalViewSet(mixins.CreateModelMixin, 
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):

    serializer_class = LoanProposalSerializer
    queryset = LoanProposal.objects.all()     
