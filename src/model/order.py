from dataclasses import dataclass


@dataclass
class Order:
    good: str
    quantity: int
    price_per_unity: int
    total: int

    @staticmethod
    def from_json(json):
        return Order(
            good=json['good'],
            quantity=json['quantity'],
            price_per_unity=json['pricePerUnit'],
            total=json['total']
        )