from datetime import datetime
import requests, os
from pprint import pprint

STATION_ID = "6178c19809e7430001ba0b75"
API_ID = os.environ["API_ID"]

# STATION_ENDPOINT = f"http://api.openweathermap.org/data/3.0/stations/{STATION_ID}?appid={API_ID}"
#
# station_data = requests.get(STATION_ENDPOINT).json()
#
# lat_encoded_int = station_data["latitude"] + 90
# long_encoded_int = station_data["longitude"] + 180
#
# print(f"Message in bits is {'{0:07b}'.format(lat_encoded_int)}{'{0:08b}'.format(long_encoded_int)}")

data = [('{0:07b}'.format(station_data["latitude"] + 90)) + ('{0:08b}'.format(station_data["longitude"] + 180))
        for station_data in requests.get(f"http://api.openweathermap.org/data/3.0/stations?appid={API_ID}").json()]

pprint([int(int_data, 2) for int_data in data])