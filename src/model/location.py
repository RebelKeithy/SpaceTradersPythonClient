from dataclasses import dataclass
from typing import List

from model.market_order import MarketOrder


@dataclass
class Location:
    symbol: str
    type: str
    name: str
    x: str
    y: str
    allows_construction: bool
    ships: List
    marketplace: List[MarketOrder]
    structures: List

    @staticmethod
    def from_json(json):
        return Location(
            symbol=json.get('symbol'),
            type=json.get('type'),
            name=json.get('name'),
            x=json.get('x'),
            y=json.get('y'),
            allows_construction=json.get('allowsConstruction'),
            ships=json.get('ships'),
            marketplace=[MarketOrder.from_json(mo) for mo in json.get('marketplace', [])],
            structures=json.get('structures')
        )