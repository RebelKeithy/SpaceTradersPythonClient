from dataclasses import dataclass
from typing import Optional, List

from model.cargo import Cargo


@dataclass
class PurchaseLocation:
    system: str
    location: str
    price: int

    @staticmethod
    def from_json(json):
        return PurchaseLocation(
            system=json['system'],
            location=json['location'],
            price=json['price']
        )

@dataclass
class Ship:
    cargo: List[Cargo]
    class_: str
    id: Optional[str]
    location: Optional[str]
    manufacturer: str
    max_cargo: int
    plating: int
    purchase_locations: Optional[List[PurchaseLocation]]
    space_available: Optional[int]
    speed: int
    type: str
    weapons: int
    x: Optional[int]
    y: Optional[int]

    @staticmethod
    def from_json(json):
        return Ship(
            cargo=[Cargo.from_json(cargo) for cargo in json.get('cargo', [])],
            class_=json.get('class'),
            id=json.get('id'),
            location=json.get('location'),
            manufacturer=json.get('manufacturer'),
            max_cargo=json.get('maxCargo'),
            plating=json.get('plating'),
            purchase_locations=[PurchaseLocation.from_json(loc) for loc in json.get('purchaseLocations', [])],
            space_available=json.get('spaceAvailable'),
            speed=json.get('speed'),
            type=json.get('type'),
            weapons=json.get('weapons'),
            x=json.get('x'),
            y=json.get('y')
        )
