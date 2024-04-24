'''HIDE THE KEYS, PASSWORDS OND OTHER IMPORTANT TOKENS
WHEN UPLOADING YOUR SCRIPT TO A HOST SERVICE'''

import os
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = os.environ.get("OWM_API_KEY") #saved as OWM_API_KEY in the particular environment

account_sid = "ACfbb246d73a1803efb706304105188b45"

auth_token = os.environ.get("AUTH_TOKEN") #saved as AUTH_TOKEN in the environment

weather_params = {
    "lat": 23.259933,
    "lon": 77.412613,
    #above is for bhopal
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Finna Rain Innit ☔️",
        from_="+165623153##",
        to="+917909705###"
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Not Finna Rain Innit ☔️",
        from_="+165623153##",
        to="+917909705###"
    )
    print(message.status)

# The required Commands - 

# ~ $ export OWM_API_KEY=e05abdf5e332a72e08f9975707c9a1##
# ~ $ python3 main.py
# queued
# ~ $ export AUTH_TOKEN=c0ddcb3e61f5c055a7c1338bad8c5## #been changed
# ~ $ python3 main.py
# queued

