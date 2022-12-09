from os import system

system("cls")

food_name = [ "Pizza", "Salad", "Soup" ]
food_price = [  100.00,   50.00, 25.00 ]

status = [ "free", "free", "free" ]
client = [     "",     "",     "" ]
order  = [     "",     "",     "" ]
bill   = [    0.0,    0.0,    0.0 ]
tip    = [    0.0,    0.0,    0.0 ]

# 1. client "John" -> 3rd table
client[2] = "John"
# HW : try to add input from keyboard
status[2] = "not-free"

client[0] = "Marry"
status[0] = "not-free"

# 2. "John" orders a soup
client_name = "John"
food_ordered_name = "Soup"
client_idx = client.index(client_name)
#print(client_idx)
order[client_idx] = food_ordered_name

food_idx = food_name.index(food_ordered_name)
bill[client_idx] = food_price[food_idx]
tip[client_idx] = bill[client_idx] * 0.1

for ti in range(len(status)):
    print(f"table {ti+1} ({status[ti]})")
    if status[ti] != "free":
        print(f"\t {client[ti]}")
        # HW : do not show this if no order
        if order[ti] != "" : 
            print(f"\t {order[ti]} -> {bill[ti]} ->tips {tip[ti]}")
        else:
            print("         Customer thinking!")   