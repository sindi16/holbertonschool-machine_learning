#!/usr/bin/env python3
"""Create a method that returns the list of ships"""

import requests


def availableShips(passengerCount):
    """Create a method that returns the list of ships"""
    url = "https://swapi-api.hbtn.io/api/starships/"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()
    ships = []

    for ship in data.get('results', []):
        ships.append(ship['name'])
    return ships
