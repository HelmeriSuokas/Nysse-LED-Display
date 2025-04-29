import requests
import base64

client_id = "1433101575045228"
client_secret = "UctF12ni9eEew9Dk6EIUMpqdjAX5t4Py"

# tekee base64 headerin
credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()


headers = {
    "Authorization": f"Basic {encoded_credentials}"
}

# testaa kirjautumisen
url = "https://data.waltti.fi/tampere/api/gtfsrealtime/v1.0/feed/servicealert"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Vastaus saatu")
    print(response.content)
else:
    print(f"Virhe: {response.status_code}")
    print(response.text)