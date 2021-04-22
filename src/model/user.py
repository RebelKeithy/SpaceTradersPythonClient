from dataclasses import dataclass
from typing import List

from model.ship import Ship


@dataclass
class User:
    username: str
    credits: int
    ships: List[Ship]
    loans: list

    @staticmethod
    def from_json(json):
        return User(
            username=json['username'],
            credits=json['credits'],
            ships=[Ship.from_json(ship) for ship in json['ships']],
            loans=json['loans']
        )
