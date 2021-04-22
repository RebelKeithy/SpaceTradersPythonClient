from dataclasses import dataclass

import requests

from model.location import Location


class LocationComponent:
    @dataclass
    class LocationInfoReponse:
        location: Location
        docked_ships: int

    def __init__(self, client):
        self.client = client

    def info(self, location: str) -> LocationInfoReponse:
        response = requests.get(f'{self.client.game_endpoint}/locations/{location}', headers=self.client.auth_headers)
        response.raise_for_status()
        return LocationInfoReponse(
            location=Location.from_json(response.json()['location']),
            docked_ships=response.json["dockedShips"]
        )
