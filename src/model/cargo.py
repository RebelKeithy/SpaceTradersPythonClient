from dataclasses import dataclass


@dataclass
class Cargo:
    good: str
    quantity: int
    total_volume: int

    @staticmethod
    def from_json(json):
        return Cargo(
            good=json.get('good'),
            quantity=json.get('quantity'),
            total_volume=json.get('totalVolume')
        )