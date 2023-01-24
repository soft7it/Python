import requests
from os import system

###########  if you would info about IP address or who is owner domain  ##########
system("cls")

while True:
    query = input("Enter a domain or IP address : ")
    url = f"http://ip-api.com/json/{query}"
    # HW : make it interactive + exit option
    res = requests.get(url)
    data = res.json()

    if data['status'] == 'success':
        #print(data)
        # print(data['country'])
        # print(data['isp'])
        print(data["status"])
        print(data["country"])
        print(data["countryCode"])
        print(data["region"])
        print(data["regionName"])
        print(data["city"])
        print(data["zip"])
        print(data["lat"])
        print(data["lon"])
        print(data["timezone"])
        print(data["isp"])
        print(data["org"])
        print(data["as"])
        print(data["query"])
    else:
        print('Not found!')
    querry = input("Would you like check again? yes/no:  ")
    if query == "no":
        break
      
          