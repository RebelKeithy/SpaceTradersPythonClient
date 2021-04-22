import datetime
from dataclasses import dataclass

from constants import LoanType, LoanStatus


@dataclass
class Loan:
    due: str
    id: str
    repaymentAmount: int
    status: LoanStatus
    type: LoanType

    @staticmethod
    def from_json(json):
        return Loan(
            due=json['due'],
            id=json['id'],
            repaymentAmount=json['repaymentAmount'],
            status=LoanStatus(json['status']),
            type=LoanType(json['type'])
        )