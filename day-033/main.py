import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")


MY_LAT = LATITUDE_COORDINATES
MY_LNG = LONGITUDE_COORDINATES
# #raising exceptions using requests module
# response.raise_for_status()

#raising exceptions using requests module
response.raise_for_status()


# data = response.json()

# longitude =  data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response1 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response1.raise_for_status
data = response1.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)

