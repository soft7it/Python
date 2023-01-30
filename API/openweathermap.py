import requests

city = input("Enter locality:  ")
KEY = ""  # https://openweathermap.org/current

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric"

res = requests.get(url)
data = res.json()

#
if data['cod'] == 200:
    temp = data['main']['temp']

    locality = data['name']

    wind_speed = data['wind']['speed']

    print(f"Weather in {locality}")
    print(f'T: {temp}C')
    print(f'Wind: {wind_speed}m/s')
elif data['cod'] == '404':
    print(f"{city} not found")
else:
    print("Not data aviable")  

########################################################

"""{"coord":{"lon":-0.1257,
          "lat":51.5085},
 "weather":[
    {"id":803,
     "main":"Clouds",
     "description":"broken clouds",
     "icon":"04d"}],
 "base":"stations",
 "main":{"temp":7.49,
         "feels_like":4.39,
         "temp_min":6.4,
         "temp_max":8.53,
         "pressure":1024,
         "humidity":72},
 "visibility":10000,
 "wind":{"speed":5.14,
         "deg":280},
 "clouds":{"all":81},
 "dt":1675073893,
 "sys":{"type":2,
        "id":2075535,
        "country":"GB",
        "sunrise":1675064547,
        "sunset":1675097090},
 "timezone":0,
 "id":2643743,
 "name":"London",
 "cod":200}  """        
