from os import system
from time import sleep
# Lift Simulation / realms simulation

# * conditionals / looping / branching
# * logic wrapping / inside-out
# * logical sequences / connections
# * HW: write the logic for no Roof and no Parking - done
# * HW: write the logic for the human inside the lift
# * HW: write the logic that draws the lift top


DIR_UP = -1
DIR_STOPPED = 0
DIR_DOWN = 1

building_roof = True
building_floors = 9
building_parking = True

lift_floor = 3
lift_open = False
lift_dir = DIR_STOPPED
lift_target_floor = 1

human_flor = 6
human_in_lift = True

#  ---|-----|---
#   R |     |
#  ---|     |---
#   9 |     |
#  ---|     |---
#   8 |     |
#  ---|     |---
#   7 |     |
#  ---|     |---
#   6 |     |
#  ---|     |---
#   5 |     |
#  ---|     |---
#   4 | < > |
#  ---||---||---
#   3 ||   ||H
#  ---||---||---
#   2 |     |
#  ---|     |---
#   1 |     |
#  ---|     |---
#   P |     |
#  ---|-----|---




# Hw: fix the bug lift bottom at the 1st floor    
# Hw: fix the bug lift indicator at the 9st floor
# HW: add code so when the lift arrives human exit
system("cls")
while True: 
    human_flor = int(input("Where is the human ? "))
    human_in_lift = input("Is human inside lift y / n ? ") == "y"
    call_lift = input("Call the lift  y / n ? ") == "y"

    if call_lift:
        if not human_in_lift:
            lift_target_floor = human_flor
        else:
            lift_target_floor = int(input("where to ? "))    

    lift_open = False

    if lift_floor < lift_target_floor:
        speed = +1
        lift_dir = DIR_UP
    if lift_floor > lift_target_floor:
        speed = -1
        lift_dir = DIR_DOWN
    if lift_floor == lift_target_floor:
        speed = 0
        # lift_dir = DIR_STOPPED
        # lift_open = True

    ### animation
    while True:

        lift_floor += speed

        if lift_floor == lift_target_floor:        
            lift_open = True
            lift_dir = DIR_STOPPED


        ##########  RENDER FRAME  ##########
        system("cls")

        if building_roof:
            print("---|-----|---")
            print(" R |     |   ")
        else:
            print("    _____")


        for floor in range(9, 0, -1):  # [9,8,7...,1]
            
        #   4 | < > |
        #  ---||---||---
        #   3 ||   ||H
        #  ---||---||---
            a = "     "
            c = "     "
            t = "     "
            s = " "

            if floor == lift_floor +1:
                if lift_dir == DIR_DOWN:
                    a = "  V  "
                elif lift_dir == DIR_UP:
                    a = "  ^  "
                elif lift_dir == DIR_STOPPED and lift_open:
                    a = " < > "

            elif floor == lift_floor:
                a = "|   |"
                t = "|---|"
                if human_in_lift:
                    a = "| H |"
            elif floor == lift_floor -1:
                t = "|---|"
            elif floor == human_flor:
                if not human_in_lift:
                    s = "H"    



            print(f"---|{t}|---") 
            print(f"{floor:^3}|{a}|{s}")

        #   4 | {a} |       floor + 1

        #  ---| {t} |---
        #   3 | {c} |{s}    flooor

        #  ---| {b} |---    floor - 1

        if building_parking:
            print("---|     |---")
            print(" P |     |   ")
            print("---|-----|---")
        else:
            print("---|-----|---")


    ##########  RENDER FRAME  ##########

        sleep(1) # atentie la ierarhie
        if lift_floor == lift_target_floor:
            break
    ###########  ANIMATION ###########    
   # sleep(1)    

# Solution ###
# * focus / centric - nucleul pe ce bazezi, de unde incepi si te concentrezi
# * enveroment specific / input
# * language
# * output / template