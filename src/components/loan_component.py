from typing import List

import requests

from constants import LoanType
from model.loan import Loan
from model.loan_opportunity import LoanOpportunity


class LoanComponent:
    def __init__(self, client):
        self.client = client

    def available_loans(self) -> List[LoanOpportunity]:
        response = requests.get(f'{self.client.game_endpoint}/loans', headers=self.client.auth_headers)
        response.raise_for_status()
        return list(map(LoanOpportunity.from_json, response.json()['loans']))

    def my_loans(self) -> List[Loan]:
        response = requests.get(f'{self.client.user_endpoint}/loans', headers=self.client.auth_headers)
        response.raise_for_status()
        return list(map(Loan.from_json, response.json()['loans']))

    def takeout_loan(self, loan_type: LoanType) -> Loan:
        params = {
            'type': loan_type.value
        }
        response = requests.post(f'{self.client.user_endpoint}/loans', headers=self.client.auth_headers, params=params)
        response.raise_for_status()
        return Loan.from_json(response.json())
