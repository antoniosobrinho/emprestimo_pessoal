from rest_framework import status
from rest_framework.test import (APITestCase, APIClient)

class LoanProposalTestCase(APITestCase):

    def test_post_loan_proposal(self):

        api_client = APIClient()

        data = {
            "name": "Jonh Cena",
            "document_number": "93682271015",
            "address" : "Street A, number 200",
            "loan_value": 10000.00
        }

        response = api_client.post(
                                f'/api/personal_loan/loan_proposal/',
                                data=data,
                                format='json'
                                )
        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)