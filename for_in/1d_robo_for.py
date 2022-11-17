from os import system

#Remarke 1d robot game -> for loop

roboX = 5
LENGTH = 10
option = ""

#game loop
while True:
    ########### 1 Draw map ############
    system("cls")
    print("\n")

    for x in range(1, LENGTH + 1):
        if x == roboX:
            print("R", end="")
        else:
            print(".", end="")

    print("\n")   

    ########### 1 Draw map ############

    ########### 2 Read input ############
    option = input(">>>")
    ########### 2 Read input ############

    ########### 3 Decide ############
    if option == "a":  # move left
        roboX -= 1
    if option == "a":  # move right
        roboX -= 1
    if option == "x":  # eXit
        system("cls")
        print("Thank you for playing!")
        break

