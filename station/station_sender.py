from datetime import datetime
import requests, random
from pprint import pprint
import os

API_ID = os.environ["API_ID"]

my_stations = requests.get(f"http://api.openweathermap.org/data/3.0/stations?appid={API_ID}").json()
my_station_details = [{
    "id": station["id"],
    "external_id": station["external_id"],
    "name": station["name"]
} for station in my_stations]

# pprint(my_station_details)

messages = ['{0:15b}'.format(random.randrange(0, 32768)) for i in range(8)]
pprint(messages)
pprint([int(int_data, 2) for int_data in messages])
station_counter = 0
for station, message in zip(my_station_details, messages):
    STATION_ID = station["id"]

    STATION_ENDPOINT = f"http://api.openweathermap.org/data/3.0/stations/{STATION_ID}?appid={API_ID}"

    lat_encoded_int = int(message[0:7], 2) - 90
    long_encoded = int(message[7:15], 2) - 180
    print(lat_encoded_int)
    print(long_encoded)

    data = requests.put(STATION_ENDPOINT, json={
        "external_id": f"HENRIETTA_TEST_{station_counter}",
        "name": "RIT's Weather Station",
        "latitude": lat_encoded_int,
        "longitude": long_encoded,
    })
    station_counter = station_counter + 1
    print(data.json())

'''
[16405, 20061, 20199, 11472, 29367, 6485, 16218, 25455]
[16405, 20061, 20199, 11472, 29367, 6485, 16218, 25455]
'''