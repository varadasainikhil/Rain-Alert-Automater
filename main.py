import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
account_sid = 'YOUR account SID'
auth_token = 'Your AUTH TOKEN'
API_KEY = "Your API KEY"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall?"
weather_params = {
    "lat": 17.385044,
    "lon": 78.486671,
    "exclude": "minutely,daily,current,alerts",
    "appid": API_KEY
}

weather_response = requests.get(url=OWM_ENDPOINT, params=weather_params)
# print(weather_response.status_code) Check if the code is not working
sliced_weather_response = weather_response.json()["hourly"][:12]  # To slice the first 12 hours
will_rain = False
for hour_data in sliced_weather_response:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
    # print(hour_data["weather"][0]["description"])

if will_rain:
    print("Bring an umbrella")
    # and set the environment variables. See http://twil.io/secure
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to Rain today, Take an umbrella",
        from_='YOUR TWILIO GENERATED PH NO',
        to='YOUR PHONE NUMBER'
    )
    print(message.sid)


