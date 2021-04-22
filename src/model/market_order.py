from dataclasses import dataclass


@dataclass
class MarketOrder:
    symbol: str
    volume_per_unit: int
    price_per_unit: int
    spread: int
    purchase_price_per_unit: int
    sell_price_per_unit: int
    quanity_available: int

    @staticmethod
    def from_json(json):
        return MarketOrder(
            symbol=json['symbol'],
            volume_per_unit=json['volumePerUnit'],
            price_per_unit=json['pricePerUnit'],
            spread=json['spread'],
            purchase_price_per_unit=json['purchasePricePerUnit'],
            sell_price_per_unit=json['sellPricePerUnit'],
            quanity_available=json['quantityAvailable']
        )