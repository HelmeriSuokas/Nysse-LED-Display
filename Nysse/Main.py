import subprocess
import os
import sys
import requests
import base64
import pandas as pd
import datetime
import time
from google.transit import gtfs_realtime_pb2

# tunnarit
client_id = "1433101575045228"
client_secret = "UctF12ni9eEew9Dk6EIUMpqdjAX5t4Py"

# auth
credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

headers = {
    "Authorization": f"Basic {encoded_credentials}"
}

# pysäkki id
target_stop_id = "0831"

# käynnistää display.py
# script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Display.py")
# subprocess.Popen([sys.executable, script_pa

# Full path to ratikka.py in samples folder!
ratikka_path = "ratikka.py"
cmd = [
    "sudo", "python3", ratikka_path,
    "--led-cols=64",
    "--led-rows=32",
    "--led-chain=1",
    "--led-parallel=1",
    "--led-scan-mode=0",
    "--led-brightness=70",
    "--led-pwm-bits=8",
    "--led-gpio-mapping=adafruit-hat",
    "--led-slowdown-gpio=4"
]
subprocess.Popen(
    cmd,
    cwd="/home/hemme/rpi-rgb-led-matrix/bindings/python/samples"
)

# GTFS tiedot
stops = pd.read_csv("stops.txt", dtype=str)
trips = pd.read_csv("trips.txt", dtype=str)
routes = pd.read_csv("routes.txt", dtype=str)
trips["trip_id"] = trips["trip_id"].str.strip()

# hakee ratikat
def hae_seuraava_ratikka():
    upcoming = []

    url = "https://data.waltti.fi/tampere/api/gtfsrealtime/v1.0/feed/tripupdate"
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    feed.ParseFromString(response.content)

    for entity in feed.entity:
        if not entity.HasField("trip_update"):
            continue

        tu = entity.trip_update

        for stu in tu.stop_time_update:
            if stu.stop_id == target_stop_id and stu.HasField("departure"):
                departure_time = datetime.datetime.utcfromtimestamp(stu.departure.time) + datetime.timedelta(hours=3)
                upcoming.append((departure_time, "???"))

    return sorted(upcoming)

# tuloste loopattuna
while True:

    next_departures = hae_seuraava_ratikka()

    if next_departures:
        now = datetime.datetime.now()  # Local time

        valid_departures = [
            (dep, route) for dep, route in next_departures
            if (dep - now).total_seconds() > 0
        ]

        if valid_departures:
            next_dep_time, route_name = valid_departures[0]
            aikaero = (next_dep_time - now).total_seconds() / 60

            with open("/tmp/ratikka_info.txt", "w") as f:
                if aikaero < 1:
                    f.write("Meni jo")
                else:
                    f.write("Opiskelija A\n")
                    f.write(f"{int(aikaero)} min")

        else:
            print("Meni jo\n")
    else:
        print("Meni jo\n")

    time.sleep(20)
