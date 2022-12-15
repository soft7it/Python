from os import system

# LEGEND:
# 0 - FREE
# 1 - RESERVED
# 2 - BOUGHT

seats = [ 0, 0, 1, 2, 0, 0, 0, 0 ]
# index   0, 1, 2,  ...........7
option = -1

while option != 0:
    # iterative count algoritm ######
    # HW : let`s say free_seats = len(seats)
    free_seats = 0
    for pi in range( len(seats) ):
        if seats[pi] == 0:
            free_seats += 1

    #  ##################################
    #  ######## PLOT ################
    system("cls")
    print()
    for pi in range( len(seats) ):
        print("", pi+1, "", end="  ")
    print()

    for pi in range( len(seats) ):
        if seats[pi] == 1:
            print("|-|", end="  ")
        elif seats[pi] == 2:
            print("|+|", end="  ")
        else:
            print("| |", end="  ")
    print("\nFree seats: ", free_seats)
    print("\n")        
    #  ######## PLOT ################   
    # 
    #  #######  SHOW MENIU  #########
    print("Meniu")         
    print("1. Book")         
    print("2. Buy")         
    print("3. Cancel")         
    print("0. Exit")         
    print("---------------------------")  

    option = int(input(">>>>> "))

    # HW : add check condition:
    # - boundaries
    # - check if the place is free
    if option == 1:
        place = int(input("Which place ? "))
        seats[ place - 1 ] = 1

    # HW :add buy, cancel  + check Only if Booked !!!  