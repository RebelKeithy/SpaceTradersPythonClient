from typing import List

import requests

from model.location import Location
from model.order import Order
from model.ship import Ship


class MarketComponent:
    def __init__(self, client):
        self.client = client

    def list(self, location: str) -> List:
        url = f'{self.client.game_endpoint}/locations/{location}/marketplace'
        response = requests.get(url, headers=self.client.auth_headers)
        response.raise_for_status()
        return Location.from_json(response.json()['location'])

    def purchase(self, ship_id: str, good: str, quantity: int):
        url = f'{self.client.user_endpoint}/purchase-orders'
        params = {
            'shipId': ship_id,
            'good': good,
            'quantity': quantity
        }
        response = requests.post(url, headers=self.client.auth_headers, params=params)
        response.raise_for_status()
        return {
            'credits': response.json()['credits'],
            'order': Order.from_json(response.json()['order']),
            'ship': Ship.from_json(response.json()['ship'])
        }

    def sell(self, ship_id: str, good: str, quantity: int):
        url = f'{self.client.user_endpoint}/sell-orders'
        params = {
            'shipId': ship_id,
            'good': good,
            'quantity': quantity
        }
        response = requests.post(url, headers=self.client.auth_headers, params=params)
        response.raise_for_status()
        return {
            'credits': response.json()['credits'],
            'order': Order.from_json(response.json()['order']),
            'ship': Ship.from_json(response.json()['ship'])
        }
