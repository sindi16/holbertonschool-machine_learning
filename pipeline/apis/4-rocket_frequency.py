#!/usr/bin/env python3
""" Uses the (unofficial) SpaceX API """
import requests


if __name__ == "__main__":
    url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(url)
    try:
        results = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: Launches data is not valid JSON")
        results = []
    rocketDict = {}
    for launch in results:
        rocket = launch.get('rocket')
        rocket_url = f'https://api.spacexdata.com/v4/rockets/{rocket}'
        rocket_response = requests.get(rocket_url)
        try:
            rocket_data = rocket_response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Warning: Rocket data for {rocket} is not valid JSON")
            continue
        rocket_name = rocket_data.get('name')
        if rocketDict.get(rocket_name) is None:
            rocketDict[rocket_name] = 1
        else:
            rocketDict[rocket_name] += 1
    rocketList = sorted(rocketDict.items(), key=lambda kv: kv[0])
    rocketList = sorted(rocketList, key=lambda kv: kv[1], reverse=True)
    for rocket in rocketList:
        print(f"{rocket[0]}: {rocket[1]}")
