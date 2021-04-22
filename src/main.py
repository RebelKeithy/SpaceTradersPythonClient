from typing import List
import pprint
import requests

from client import SpaceTraderClient
from utils.print import print_list
from utils.print import print_systems

from halo import Halo
import time

USERNAME = "RebelKeithy"
TOKEN = "<REDACTED>"

client = SpaceTraderClient(USERNAME, TOKEN)
user = client.get_info()


def update_user():
    global user
    user = client.get_info()


def get_cargo_amount(good: str):
    for cargo in user.ships[0].cargo:
        if cargo.good == good:
            return cargo.total_volume
    return 0


def restock():
    volume = user.ships[0].space_available
    if volume > 0:
        result = client.purchase_orders(ship.id, 'METALS', volume)
        print(f'Credits: {result["credits"]}')
        print(f'Ships: {result["order"]}')
        print(f'Loans: {result["ship"]}')
        user.ships[0] = result['ship']


def unload():
    metals = get_cargo_amount('METALS')
    if metals > 0:
        result = client.sell_order(ship.id, 'METALS', metals)
        print(f'Credits: {result["credits"]}')
        print(f'Ships: {result["order"]}')
        print(f'Loans: {result["ship"]}')
        user.ships[0] = result['ship']


def refuel(amount=27):
    fuel = get_cargo_amount('FUEL')
    print(f"We have {fuel} fuel")
    if fuel < amount:
        result = client.purchase_orders(ship.id, 'FUEL', amount - fuel)
        print(f'Credits: {result["credits"]}')
        print(f'Ships: {result["order"]}')
        print(f'Loans: {result["ship"]}')
        user.ships[0] = result['ship']
    else:
        print("Already Full of Fuel")


def travel_to(location):
    flight_plan = client.flights.submit_flight_plan(user.ships[0].id, location)
    print(flight_plan)

    spinner = Halo(text='Traveling', spinner='dots')
    spinner.start()
    for i in range(flight_plan.time_remaining_in_seconds, 0, -1):
        spinner.text = f"Traveling: {i}"
        time.sleep(1)
    spinner.stop()

    update_user()



if __name__ == '__main__':
    ship = user.ships[0]
    print(f'Credits: {user.credits}')
    print(f'Ships: {str(user.ships)}')
    print(f'Loans: {str(user.loans)}')

    while True:
        travel_to('OE-NY')
        refuel()
        restock()

        travel_to('OE-KO')
        unload()
        refuel()

