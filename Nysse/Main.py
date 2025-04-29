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

# GTFS tiedot
stops = pd.read_csv("stops.txt")
# stop_times = pd.read_csv("stop_times.txt")
trips = pd.read_csv("trips.txt")
routes = pd.read_csv("routes.txt")

# hakee ratikat
def hae_seuraava_ratikka():
    upcoming = []

    url = "https://data.waltti.fi/tampere/api/gtfsrealtime/v1.0/feed/tripupdate"
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(url, headers=headers)
    feed.ParseFromString(response.content)

    for entity in feed.entity:
        if not entity.HasField("trip_update"):
            continue

        tu = entity.trip_update

        for stu in tu.stop_time_update:
            if stu.stop_id != target_stop_id:
                continue

            if stu.HasField("departure"):
                ts = stu.departure.time
                departure_time = datetime.datetime.fromtimestamp(ts)

                if departure_time < datetime.datetime.now():
                    continue

                trip_id = tu.trip.trip_id
                trip_row = trips[trips["trip_id"].str.endswith(trip_id.split("_")[-1])]
                if trip_row.empty:
                    continue

                route_id = trip_row.iloc[0]["route_id"]
                route_row = routes[routes["route_id"] == route_id]
                route_name = route_row.iloc[0]["route_short_name"] if not route_row.empty else "?"

                upcoming.append((departure_time, route_name))

    return sorted(upcoming) if upcoming else []

# tuloste loopattuna
while True:
    next_departures = hae_seuraava_ratikka()

    if next_departures:
        now = datetime.datetime.now()

        # Tulevaisuuden lähtöjen filtteri
        valid_departures = [
            (dep, route) for dep, route in next_departures
            if (dep - now).total_seconds() > 0
        ]

        if valid_departures:
            next_dep_time, route_name = valid_departures[0]
            aikaero = (next_dep_time - now).total_seconds() / 60

            if aikaero < 1:
                print("Meni jo\n")
            else:
                print("Opiskelija A")
                print(f"{int(aikaero)} min")
        else:
            print("Meni jo\n")
    else:
        print("MITÄ VITTUA\n")

    time.sleep(20)