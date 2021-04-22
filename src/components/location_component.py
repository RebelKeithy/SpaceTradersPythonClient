from dataclasses import dataclass
from typing import List

import requests

from model.location import Location
from model.system import System


@dataclass
class LocationInfoResponse:
    location: Location
    docked_ships: int


class LocationComponent:

    def __init__(self, client):
        self.client = client

    def info(self, location: str) -> LocationInfoResponse:
        response = requests.get(f'{self.client.game_endpoint}/locations/{location}', headers=self.client.auth_headers)
        response.raise_for_status()
        return LocationInfoResponse(
            location=Location.from_json(response.json()['location']),
            docked_ships=response.json()["dockedShips"]
        )

    def ships(self, location: str) -> Location:
        response = requests.get(f'{self.client.game_endpoint}/locations/{location}/ships', headers=self.client.auth_headers)
        response.raise_for_status()
        return Location.from_json(response.json()['location'])

    def locations(self, system: str) -> List[Location]:
        response = requests.get(f'{self.client.game_endpoint}/systems/{system}/locations', headers=self.client.auth_headers)
        response.raise_for_status()
        return [Location.from_json(loc) for loc in response.json()['locations']]

    def systems(self):
        response = requests.get(f'{self.client.game_endpoint}/systems', headers=self.client.auth_headers)
        response.raise_for_status()
        return [System.from_json(s) for s in response.json().get('systems', [])]
