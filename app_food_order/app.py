from restaurant import *

### contains order data
order = {
    "items": []
}

################ Bisnes code _MAIN ###############
food = loadFood()  # lista care incepe de la 0,1,2....
while True: 
    option = printMeniu()

    if option == 0:
        break
    ################    
    if option == 1:
        printFood(food)
        input("Hit, Enter to continue")
    #################
    if option == 2:
        selected_i = int(input("which item: ")) - 1
        print(f"you have selected <<{food[selected_i]['name']}>>")
        quantity = int(input("How many: "))
        
        if quantity <= food[selected_i]['aviabl']:
            print(f"order is aviabl{quantity}")        
            
            # HW : IF+ELSE -> CHECK "AVIABL"
            price_per_item = quantity * food[selected_i]['price']['amount']
            print(f" <<{food[selected_i]['name']}>> x {quantity} = {price_per_item:8.2f} {food[selected_i]['price']['currency']}")
            yes = input("confirm if you agree yes -y/no -n")
            if "y" == yes:
                print(f"Please pay for food. ")
                #######  order rec in list######################
                order['items'].append( {food[selected_i]['name']} )
                order['items'].append( {quantity} )
                order['items'].append( {price_per_item} )
                ################################################                                
            elif "n" == yes:
                print("You could try onother one item")        
            # HW: ask for confirmation (yes/no)? 28:00min video?
            # daca ai trecut de confirmare, adaugati pe pozitia order item (.append), formam nou dictionat
            #contine: denumire, quantity, total per total(amunt+currency)
            print(order['items'][0], order['items'][1], order['items'][2])
            input("Hit, Enter to continue")
            
        else:  # ask order!!
            print(f"Sorry, aviable is only {food[selected_i]['aviabl']}")
            input("Hit, Enter to continue")