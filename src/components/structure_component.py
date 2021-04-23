from typing import Any

import requests


class StructureComponent:
    def __init__(self, client):
        self.client = client

    # TODO: Needs testing
    def create(self, location: str, type: str) -> Any:
        url = f'{self.client.user_endpoint}/structures'
        params = {'location': location, 'type': type}
        response = requests.post(url, headers=self.client.auth_headers, params=params)
        response.raise_for_status()
        return response.json()

    # TODO: Needs testing
    def deposit(self, structure_id: str, ship_id: str, good: str, quantity: int) -> Any:
        url = f'{self.client.user_endpoint}/structures/{structure_id}/deposit'
        params = {'shipId': ship_id, 'good': good, 'quantity': quantity}
        response = requests.post(url, headers=self.client.auth_headers, params=params)
        response.raise_for_status()
        return response.json()

    # TODO: Needs testing
    def info(self, structure_id: str):
        url = f'{self.client.user_endpoint}/structures/{structure_id}'
        response = requests.get(url, headers=self.client.auth_headers)
        response.raise_for_status()
        return response.json()

    # TODO: Needs testing
    def list(self):
        url = f'{self.client.user_endpoint}/structures'
        response = requests.get(url, headers=self.client.auth_headers)
        response.raise_for_status()
        return response.json()

    # TODO: Needs testing
    def transfer(self, structure_id: str, ship_id: str, good: str, quantity: int):
        url = f'{self.client.user_endpoint}/structures/{structure_id}/transfer'
        params = {'shipId': ship_id, 'good': good, 'quantity': quantity}
        response = requests.post(url, headers=self.client.auth_headers, params=params)
        response.raise_for_status()
        return response.json()
