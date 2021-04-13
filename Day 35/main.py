import requests
from twilio.rest import Client


API_ENDPOINT = "http://api.openweathermap.org/data/2.5/onecall"
API_KEY = "your api key from openweathermap profile"
ACCOUNT_SID = "twilio account sid"
AUTH_TOKEN = "twilio auth token"


weather_param = {
    "lat": -4.441931,
    "lon": 15.266293,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}


response = requests.get(API_ENDPOINT, params=weather_param)
response.raise_for_status()
weather_data = response.json()


will_rain = False


weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages \
                .create(
                     body="It's going to rain today. Make sure to bring an ☂",
                     from_='your twiilio sample number',
                     to='your twilio verified number'
                 )
    print(message.status)