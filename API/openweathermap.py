import requests

city = input("Enter locality:  ")
KEY = ""  # https://openweathermap.org/current

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric"

res = requests.get(url)
data = res.Json()

#
if data['cod'] == 200:
    temp = data['main']['temp']

    locolity = data['name']

    wind_speed = data['wind']['speed']

    print(f"Weather in {locality}")
    print(f'T: {temp}C')
    print(f'Wind: {wind_speed}m/s')
elif data['cod'] == '404':
    print(f"{city} not found")
else:
    print("Not data aviable")  
