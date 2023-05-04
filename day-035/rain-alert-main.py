import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = API_KEY

weather_params = {
    "lat": LATITUDE_COORDINATES,
    "lon": LONGITUDE_COORDINATES,
    "appid": api_key
}

reqeusts.get(OWM_endpoint, params=weather_params)
print(response.status_code)