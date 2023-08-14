import requests
apiname= "WeatherAPI"
lat=""
lon=""
part="current"

apikey = "8f36e909a1f36b29835330defb4752a2"
api=f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={apikey}"

# https://openweathermap.org/api/geocoding-api
# https://openweathermap.org/api/one-call-3