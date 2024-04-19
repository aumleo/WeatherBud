import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "e05abdf5e332a72e08f9975707c9a1af"
account_sid = "ACfbb246d73a1803efb706304105188b45"
auth_token = "c0ddcb3e61f5c055a7c1338bad8c569f"

weather_params = {
    "lat": 23.259933,
    "lon": 77.412613,
    #above is for Bhopal 
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
        from_="+16562315328",
        to="+917909705494"
    )
    print(message.status)

#Hosted Through PythonAnywhere, for 7:00 am everyday
