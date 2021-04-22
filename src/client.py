from typing import List

import requests

from components.flight_component import FlightComponent
from components.loan_component import LoanComponent
from components.location_component import LocationComponent
from constants import LoanType
from model.flight_plan import FlightPlan
from model.loan import Loan
from model.loan_opportunity import LoanOpportunity
from model.location import Location
from model.order import Order
from model.ship import Ship
from model.system import System
from model.user import User

URL = "https://api.spacetraders.io"


class SpaceTraderClient:

    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token
        self.flights: FlightComponent = FlightComponent(self)
        self.loans: LoanComponent = LoanComponent(self)
        self.locations: LocationComponent = LocationComponent(self)

    @property
    def auth_headers(self):
        return {
            'authorization': f'Bearer {self.token}'
        }

    @property
    def game_endpoint(self): return f'{URL}/game'

    @property
    def user_endpoint(self): return f'{URL}/users/{self.username}'

    def get_info(self) -> User:
        response = requests.get(f'{self.user_endpoint}', headers=self.auth_headers)
        response.raise_for_status()
        return User.from_json(response.json()['user'])

    def register(self) -> str:
        response = requests.post(f"{self.user_endpoint}/token")
        if response.status_code == 409:
            raise Exception(f'Username "{self.username}" has already been claimed')
        response.raise_for_status()
        self.token = response.json()['token']
        return response.json()['token']

    def ships(self) -> List[Ship]:
        response = requests.get(f'{self.game_endpoint}/ships', headers=self.auth_headers)
        response.raise_for_status()
        return list(map(Ship.from_json, response.json()['ships']))

    def purchase_ship(self, type_: str, location: str):
        params = {
            'location': location,
            'type': type_
        }
        response = requests.post(f'{self.user_endpoint}/ships', headers=self.auth_headers, params=params)
        response.raise_for_status()
        print(response.text)
        return Ship.from_json(response.json())

    def purchase_orders(self, ship_id: str, good: str, quantity: int):
        params = {
            'shipId': ship_id,
            'good': good,
            'quantity': quantity
        }
        response = requests.post(f'{self.user_endpoint}/purchase-orders', headers=self.auth_headers, params=params)
        response.raise_for_status()
        return {
            'credits': response.json()['credits'],
            'order': Order.from_json(response.json()['order']),
            'ship': Ship.from_json(response.json()['ship'])
        }

    def marketplace(self, location: str) -> List:
        response = requests.get(f'{self.game_endpoint}/locations/{location}/marketplace', headers=self.auth_headers)
        response.raise_for_status()
        return Location.from_json(response.json()['location'])

    def sell_order(self, ship_id: str, good: str, quantity: int):
        params = {
            'shipId': ship_id,
            'good': good,
            'quantity': quantity
        }
        response = requests.post(f'{self.user_endpoint}/sell-orders', headers=self.auth_headers, params=params)
        response.raise_for_status()
        return {
            'credits': response.json()['credits'],
            'order': Order.from_json(response.json()['order']),
            'ship': Ship.from_json(response.json()['ship'])
        }
