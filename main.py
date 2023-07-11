import requests
from twilio.rest import Client
# import os to access environment variables
import os
open_weather_map_endpoint = "https://api.openweathermap.org/data/2.8/onecall"

# api keys prevent users from abusing the # of api calls for free
# API KEY

appid = os.environ.get("API_KEY") #OR "4b5051953be42acd61bb490707887543" you must manually add the API_KEY via the terminal

# find latitude and longitude coordinates via latlong.net
lat = 38.101089

lon = -122.254959

# based on documentation for OWM One Call API, the required parameters are lat, lon, and appid

parameters = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily",
    "appid": appid
}

response = requests.get(url=open_weather_map_endpoint, params=parameters)
# ?lat={lat}&lon={lon}&exclude={part}&appid={API key}

# returns a status code to show whether call was a success or there is an error
print(response.status_code)
# OR
#response.raise_for_status()

#display response as a json file
weather_data = response.json()
print(weather_data)

# Copy weather_data/JSON in the response console and paste it into jsonviewer.stack.hu
# "Text" tab to view the JSON in a more organized form in the "Viewer" tab

# Go back and modify parameters to exclude current,minutely,daily (no space after the comma) data

# Modify JSON file to take the next 12 hours of data

next_12_hours_data = weather_data["hourly"][:12]
print(next_12_hours_data)

# Create loop to go thru data and identify if there is rain in the next 12 hours

will_rain = False

for hour in next_12_hours_data:
    if next_12_hours_data[hour]["weather"][0]["id"] < 700:
        will_rain = True

# To send rain alert via SMS you must install twilio.rest library and import Client module
     # Get a account_sid and auth_token from twilio
ACCOUNT_SID = "ACc9563c4a0df11b1cb81200a716b8620b"
AUTH_TOKEN = "da4310b1ee89f5bfc6b5c6e5bb36fad2"

# To send a request use this code:
    # from twilio.rest import Client
    #
    # account_sid = 'ACc9563c4a0df11b1cb81200a716b8620b'
    # auth_token = '[AuthToken]'
    # client = Client(account_sid, auth_token)
    #
    # message = client.messages.create(
    #     to='+17133519231'
    # )
    #
    # print(message.sid)

if will_rain:
    print("Bring an umbrella!")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        to='+1{insert your phone number here}',
        from_='+1{insert your twilio number here}',
        body="It's going to rain today! Remember to bring an umbrella ☂💧!"
    )
    print(message.status)


# To store environment variables go to the terminal command shell and type "set"
# Then


