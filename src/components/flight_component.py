import requests

from model.flight_plan import FlightPlan


class FlightComponent:
    def __init__(self, client):
        self.client = client

    def active_flight_plans(self, system: str):
        url = f'{self.client.game_endpoint}/systems/{system}/flight-plans'
        response = requests.get(url, headers=self.client.auth_headers)
        response.raise_for_status()
        return [FlightPlan.from_json(flight_plan) for flight_plan in response.json()['flightPlans']]

    def submit_flight_plan(self, ship_id: str, destination: str):
        url = f'{self.client.user_endpoint}/flight-plans'
        params = {
            'shipId': ship_id,
            'destination': destination
        }
        response = requests.post(url, headers=self.client.auth_headers, params=params)
        response.raise_for_status()
        return FlightPlan.from_json(response.json()['flightPlan'])

    def get_flight_plan(self, flight_plans_id: str):
        url = f'{self.client.user_endpoint}/flight-plans/{flight_plans_id}'
        response = requests.get(url, headers=self.client.auth_headers)
        response.raise_for_status()
        return FlightPlan.from_json(response.json()['flightPlan'])
