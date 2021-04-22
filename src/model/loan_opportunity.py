from dataclasses import dataclass

from constants import LoanType


@dataclass
class LoanOpportunity:
    amount: int
    collateralRequired: bool
    rate: int
    term_in_days: int
    type: LoanType

    @staticmethod
    def from_json(json):
        return LoanOpportunity(
            amount=json['amount'],
            collateralRequired=json['collateralRequired'],
            rate=json['rate'],
            term_in_days=json['termInDays'],
            type=LoanType(json['type'])
        )