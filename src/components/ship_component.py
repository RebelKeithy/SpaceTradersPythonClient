from dataclasses import dataclass
from typing import Optional, List

import requests

from model.cargo import Cargo
from model.ship import Ship


@dataclass
class JettisonResult:
    good: str
    quantity_remaining: int
    ship_id: str

    @staticmethod
    def from_json(json):
        return JettisonResult(
            good=json.get('good'),
            quantity_remaining=json.get('quantityRemaining'),
            ship_id=json.get('shipId')
        )

@dataclass
class TransferCargoResult:
    to_ship: Ship
    from_ship: Ship

    @staticmethod
    def from_json(json):
        return TransferCargoResult(
            to_ship=Ship.from_json(json.get('toShip')),
            from_ship=Ship.from_json(json.get('fromShip'))
        )


class ShipComponent:
    def __init__(self, client):
        self.client = client

    # TODO: needs to be tested
    def buy(self, location: str, type_: str) -> Ship:
        url = f'{self.client.user_endpoint}/ships'
        params = {'location': location, 'type': type_}
        response = requests.post(url, headers=self.client.auth_headers, params=params)
        response.raise_for_status()
        return Ship.from_json(response.json()['ship'])

    def available(self, class_: Optional[str] = None) -> List[Ship]:
        url = f'{self.client.game_endpoint}/ships'
        params = {'class': class_}
        response = requests.get(url, headers=self.client.auth_headers, params=params)
        response.raise_for_status()
        return list(map(Ship.from_json, response.json()['ships']))

    def info(self, ship_id: str) -> Ship:
        url = f'{self.client.user_endpoint}/ships/{ship_id}'
        response = requests.get(url, headers=self.client.auth_headers)
        response.raise_for_status()
        return Ship.from_json(response.json()['ship'])

    def list(self) -> List[Ship]:
        url = f'{self.client.user_endpoint}/ships'
        response = requests.get(url, headers=self.client.auth_headers)
        response.raise_for_status()
        return list(map(Ship.from_json, response.json()['ships']))

    def jettison_cargo(self, ship_id: str, good: str, quantity: int) -> JettisonResult:
        url = f'{self.client.user_endpoint}/ships/{ship_id}/jettison'
        params = {'good': good, 'quantity': quantity}
        response = requests.put(url, headers=self.client.auth_headers, params=params)
        response.raise_for_status()
        return JettisonResult.from_json(response.json())

    # TODO: Needs testing
    def scrap(self, ship_id: str):
        url = f'{self.client.user_endpoint}/ships/{ship_id}'
        response = requests.delete(url, headers=self.client.auth_headers)
        print(response.text)
        return response.json()

    # TODO: Needs testing
    def transfer_cargo(self, from_ship_id: str, to_ship_id: str, good: str, quantity: str) -> TransferCargoResult:
        url = f'{self.client.user_endpoint}/ships/{from_ship_id}/transfer'
        params = {'toShipId': to_ship_id, 'good': good, 'quantity': quantity}
        response = requests.put(url, headers=self.client.auth_headers, params=params)
        print(response.text)
        return TransferCargoResult(response.json())
