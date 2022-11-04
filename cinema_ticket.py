from os import system

# Data
m_title_1 = "Avatar 2"
m_title_2 = "Terminator 9"
m_title_3 = "Titanic Zombi"

m_1_ticket_cost_a = 100.00
m_1_ticket_cost_b = 120.00
m_1_ticket_cost_c = 105.00
m_1_ticket_cost_d = 110.00
m_1_ticket_cost_e = 115.00
m_1_ticket_cost_f = 125.00


# HW1 : use variables for Hour / time

system("cls") # clear

# hours movie
hour_a = "18:00"
hour_b = "20:00"
hour_c = "15:00"
hour_d = "17:00"
hour_e = "22:00"
hour_f = "21:00"

# Movie Board
print(
f"""
1.{m_title_1}
    a. {hour_a}
    b. {hour_b}
2.{m_title_2}
    a. {hour_d}
    b. {hour_e}
3.{m_title_3}
    a. {hour_c}
    b. {hour_f}
""")

movie_number = input("Choose a movie: ") # 1

if movie_number == "1":
    print(f"You have choosen {m_title_1}")
    time = input("Choose time: ")
    if time == "a":
        print(f"time: {hour_a}, ticket cost {m_1_ticket_cost_a}")
        cost = m_1_ticket_cost_a
    if time == "b":
        print(f"time: {hour_b}, ticket cost {m_1_ticket_cost_b}")
        cost = m_1_ticket_cost_b

    amount = int(input("How many tickets: "))    
    total = amount * cost
    print(f"{amount} x {cost} = {total}")
#################################################

if movie_number == "2":
    print(f"You have choosen {m_title_2}")
    time = input("Choose time: ")
    if time == "a":
        print(f" time: {hour_d}, ticket cost {m_1_ticket_cost_d}")
        cost = m_1_ticket_cost_d
    if time == "b":
        print(f"time: {hour_e}, ticket cost {m_1_ticket_cost_e}") 
        cost = m_1_ticket_cost_e

    amount = int(input("How many tickets: "))
    total = amount * cost
    print(f"{amount} x {cost} = {total}")   
 ###############################################       

if movie_number == "3":
    print(f"You have choosen {m_title_3}")
    time = input("Choose time: ")
    if time == "a":
        print(f"time: {hour_c}, ticket cost {m_1_ticket_cost_c}")
        cost = m_1_ticket_cost_c
    if time == "b":
        print(f"time: {hour_f}, ticket cost {m_1_ticket_cost_f}")   
        cost = m_1_ticket_cost_f

    amount = int(input("How many tickets: "))
    total = amount * cost   
    print(f"{amount} x {cost} = {total}")  
