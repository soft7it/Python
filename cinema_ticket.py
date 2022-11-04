from os import system

# Data
m_title_1 = "Avatar 2"
m_title_2 = "Terminator 9"
m_title_3 = "Titanic Zombi"

m_1_ticket_cost_a = 100.00
m_1_ticket_cost_b = 120.00

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
    a. 18:00
    b. 20:00
2.{m_title_2}
    a. 17:00
    b. 22:00
3.{m_title_3}
    a. 15:00
    b. 23:00
""")

movie_number = input("Choose a movie: ") # 1

if movie_number == "1":
    print(f"You have choosen {m_title_1}")
    time = input("choose time: ")
    if time == "a":
        print(f"time: 18:00, ticket cost {m_1_ticket_cost_a}")
        cost = m_1_ticket_cost_a
    if time == "b":
        print(f"time: 20:00, ticket cost {m_1_ticket_cost_b}")
        cost = m_1_ticket_cost_b

    amount = int(input("How many tickets: "))    
    total = amount * cost
    print(f"{amount} x {cost} = {total}")
    




if movie_number == "2":
    print(f"You have choosen {m_title_2}")

if movie_number == "3":
    print(f"You have choosen {m_title_3}")