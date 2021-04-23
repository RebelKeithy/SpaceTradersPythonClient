import requests

from components.flight_component import FlightComponent
from components.loan_component import LoanComponent
from components.location_component import LocationComponent
from components.market_component import MarketComponent
from components.ship_component import ShipComponent
from components.structure_component import StructureComponent
from model.user import User

URL = "https://api.spacetraders.io"


class SpaceTraderClient:

    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token
        self.flights: FlightComponent = FlightComponent(self)
        self.loans: LoanComponent = LoanComponent(self)
        self.locations: LocationComponent = LocationComponent(self)
        self.market: MarketComponent = MarketComponent(self)
        self.ships: ShipComponent = ShipComponent(self)
        self.structures: StructureComponent = StructureComponent(self)

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


