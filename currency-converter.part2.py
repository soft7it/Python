# App where :
# IN money amount
# IN currency
# OUT money amount

input_currency = input("Choose currency EUR/USD/MDL/ROU: ")  # USD

input_amount = float(input("Enter amount: "))

rate_USD_to_EUR = 0.8
rate_EUR_to_USD = 1.25
rate_EUR_to_MDL = 21.25
rate_MDL_to_EUR = 21.25
rate_EUR_to_ROU = 0.25
rate_ROU_to_EUR = 4.85

if input_currency == "USD":
    moneyEUR = input_amount / rate_EUR_to_USD
    print("You have got: ", round(moneyEUR,2), "EUR")

elif input_currency == "EUR":
    moneyUSD = input_amount / rate_USD_to_EUR
    print("You have got: ", round(moneyUSD,2), "USD")  # float(moneyUSD, 2)

elif input_currency == "MDL":
    moneyEUR_MDL = input_amount / rate_EUR_to_MDL
    print("You have got: ", round(moneyEUR_MDL,2), "EUR")

elif input_currency == "MDL-EUR":
    moneyMDL_EUR = input_amount * rate_MDL_to_EUR
    print("You have got: ", round(moneyMDL_EUR, 2), "MDL")

elif input_currency == "ROU":
    moneyEUR_ROU = input_amount * rate_ROU_to_EUR
    print("You have got: ", round(moneyEUR_ROU,2), "ROU")

elif input_currency == "ROU-EUR":
    moneyROU_EUR = input_amount * rate_EUR_to_ROU
    print("You have got: ", round(moneyROU_EUR,2), "EUR")
# else:
#     print("YOU COULD ONLY OUR VALUTE CONVERTET. ")
# problem cu lowcase si uper case!
