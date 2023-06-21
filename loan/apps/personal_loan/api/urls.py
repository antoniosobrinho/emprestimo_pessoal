from django.urls import include, re_path
from rest_framework import routers
from apps.personal_loan.api.viewsets import LoanProposalViewSet

router = routers.SimpleRouter()
router.register(r'loan_proposal', LoanProposalViewSet, basename='loan_proposal')

urlpatterns = [
    re_path(r'^', include(router.urls))
]