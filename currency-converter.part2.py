# App where :
# IN money amount
# IN currency
# OUT money amount

input_currency = input("Choose currency EUR/USD/MDL/ROU: ") #USD

input_amount = float(input("Enter amount: "))

rate_USD_to_EUR = 0.8
rate_EUR_to_USD = 1.25
rate_EUR_to_MDL = 21.25
rate_MDL_to_EUR = 1
rate_EUR_to_ROU = 0.25
rate_ROU_to_EUR = 4.85

if input_currency == "USD":
    moneyEUR = input_amount / rate_EUR_to_USD
    print("You have got: ", moneyEUR, "EUR")
elif input_amount == "EUR":
    moneyUSD = input_amount / rate_USD_to_EUR
    print("You have got: ", moneyUSD, "USD")
elif input_amount == "MDL":
    moneyEUR_MDL = input_amount / rate_EUR_to_MDL
    print("You have got: ", moneyEUR_MDL, "EUR")
elif input_amount == "EUR":
    moneyUSD = input_amount / rate_USD_to_EUR
    print("You have got: ", moneyUSD, "EUR")
elif input_amount == "ROU":
    moneyEUR_ROU = input_amount / rate_EUR_to_ROU
    print("You have got: ", moneyEUR_ROU, "ROU")
else: 
    moneyROU_EUR = input_amount / rate_ROU_to_EUR
    print("You have got: ", moneyROU_EUR, "EUR")
