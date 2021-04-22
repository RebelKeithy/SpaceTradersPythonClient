from dataclasses import dataclass
from typing import List

from model.location import Location


@dataclass
class System:
    symbol: str
    name: str
    locations: List[Location]

    @staticmethod
    def from_json(json):
        return System(
            symbol=json.get('symbol'),
            name=json.get('name'),
            locations=[Location.from_json(l) for l in json.get('locations', [])]
        )