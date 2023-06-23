from celery import shared_task
from apps.personal_loan.models import LoanProposal
from apps.personal_loan.choices import LoanStatusChoices
import random

@shared_task
def rating_loan(proposal_id):

    proposal = LoanProposal.objects.filter(id = proposal_id)

    if proposal:
        proposal = proposal.first()

        accept_proposal = random.randrange(2)

        if accept_proposal:
            status = LoanStatusChoices.ACCEPTED.value
        else:
            status = LoanStatusChoices.REFUSED.value

        proposal.status = status
        proposal.save()