import requests
# search in google how to install pip in python windows -> for fix requests
# https://pypi.org/  # module de projects !!!!!

date = "16.01.2023"

url = f"https://www.bnm.md/ro/export-official-exchange-rates?date={date}"

res = requests.get(url)
data = res.text  # . text folosim saal cpnverteze din format CSV

lines = data.split("\r\n")  # str.split()  -> list[]

# print(lines)
used_rate = 0
euro_rate = 0

for l in lines[ 3: -5 ]:    # sublist [startindex : endindex]
    currency = l.split(";") # unde gaseste ; le sterge!
    if currency[2] == "USD":
        used_rate = float( currency[4].replace(",",".") )
    if currency[2] == "EUR":
        euro_rate = float( currency[4].replace(",",".") )    

print("USD: ", used_rate)
print("EURO: ", euro_rate)



# HW : add interactivity
#      choose source currency USD/EUR/MDL
#      input amount < user
#      choose destination currency USD/EUR/MDL
#      output amount > user
