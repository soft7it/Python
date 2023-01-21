import requests
from os import system

date = "16.01.2023"

url = f"https://www.bnm.md/ro/export-official-exchange-rates?date={date}"

res = requests.get(url)
data = res.text  # . text folosim saal cpnverteze din format CSV

print(type(data)) # verificam tipul de date
# print(data)
lines = data.split("\r\n")  # str.split()  -> list[]

# print(lines)
used_rate = 0
euro_rate = 0
gbp_rate = 0

for l in lines[ 3: -5 ]:    # sublist [startindex : endindex]
    currency = l.split(";") # unde gaseste ; le sterge!
    if currency[2] == "USD":
        used_rate = float( currency[4].replace(",",".") )
    if currency[2] == "EUR":
        euro_rate = float( currency[4].replace(",",".") )    
    if currency[2] == "GBP":
        gbp_rate = float( currency[4].replace(",",".") )    

# print("USD: ", used_rate)
# print("EURO: ", euro_rate)
system("cls")

###########  HW  ##########################################
while True:
    user = input("Choose source currency USD/EUR/GBP=MDL : ")
    print(user)
    how_many = int(input("How many do you have convert : "))
    if user == "USD":
        # used_rate
        print("for 1 ->USD: ", used_rate, "Lei." )
        total_amount = how_many * used_rate
        print(total_amount)
    elif user == "EUR":
        # euro_rate
        print("for 1 ->EURO: ", euro_rate, "Lei.")
        total_amount = how_many * euro_rate
        print(total_amount)
    elif user == "GBP":
        # euro_rate
        print("for 1 ->GBP: ", gbp_rate, "Lei.")
        total_amount = how_many * gbp_rate
        print(total_amount)
    contin = input("Do you want to continue Yes/No? ")
    if contin == "Yes" :
        pass
    else:
        print("Thank you for your time, see you.")
        break    




# HW : add interactivity
#      choose source currency USD/EUR/MDL
#      input amount < user
#      choose destination currency USD/EUR/MDL
#      output amount > user
