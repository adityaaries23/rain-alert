import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
parameters = {
        "lat": -7.4664,
        "lon": 112.4338,
        "appid": API_KEY,
        "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"]
data_12 = [n["weather"][0]["id"] for n in data[0:12]]
is_rain = False
for d in data_12:
    if d < 700:
        is_rain = True

if is_rain:
    print("Bring umbrella")
    client = Client(account_sid, auth_token)
    text = client.messages.create(
        body="Today will be rain, don't forget bring umbrella",
        from_="+17652956708",
        to="+6281391589952"
    )
    print(text.status)
else:
    print("Today is good day")
