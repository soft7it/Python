from os import system
# Solving the situation when a client want to pay for a service
# - trying to pay by cash
# - trying to pay by card
# - trying to pay by cryptocurrency

# HW1: 
# Update the flowchart
# -* maybe convert crypto to chash / card

service_price = 100

# clear some :
system("cls")

# client_cash_amount = 50
# client_card_amount = 150
# client_crypto_amount = 250
#check amount crypto to converting
crypto_1_coin = 5 # 5 din 100 echivalentul valorii


# prma intrebare
client_cash_amount = int(input("enter cash amount: "))
if client_cash_amount >= service_price:
    print("CASH Payment success!!!")
else:
    print("CASH Payment FAILURE!!!")    

    # intrebarea 2 CU CARD:
    client_card_amount = int(input("enter card amount: "))
    if client_card_amount >= service_price:
        print("CARD PAYMENT SUCCESS!!!")
    else:
        print("CARD PAYMENT FAILURE!!!")    
        # intrebarea 3 crypto:
        client_crypto_amount = int(input("enter crypto amount: "))
        #mentine ierarhia operatiunilor altfel nu merge !!!
        total_cryto = crypto_1_coin * client_crypto_amount
        if total_cryto >= service_price:
            print("Payment crypto success!!!")
        else:
            print("Payment crypto FAILURE!!!")  
