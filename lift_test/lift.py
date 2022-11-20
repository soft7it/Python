from os import system
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

human_flor = 3
human_in_lift = False

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
#   4 |     |
#  ---||---||---
#   3 ||   ||H
#  ---||---||---
#   2 |     |
#  ---|     |---
#   1 |     |
#  ---|     |---
#   P |     |
#  ---|-----|---


##########  RENDER FRAME  ##########
system("cls")

if building_roof:
    print("---|-----|---")
    print(" R |     |   ")
else:
    print("    _____")    


for floor in range(9,0,-1):  # [9,8,7...,1]

    # partea de jos a liftului
    if floor == lift_floor:
        b = "|---|"
    else:
        b = "     "
    
    if floor == lift_floor - 1:
        b = "|---|"
   
    print(f"---|{b}|---")
   
    # print(" ---|     |--- ")

    if floor == human_flor and not human_in_lift:
       h = " H  "
    else:
        h = "    "

        
                                    # print(f" {floor:^3}|     |{h}")

                                    # if floor == human_flor:
                                    #     print(f" {floor:^3}|     | H ")
                                    # else:
                                    #     print(f" {floor:^3}|     |   ")  # codul lucreaza si e explecit
    # indicator
    if floor == lift_floor + 1:
        if lift_open:
            l = " < > "
        else:
            if lift_dir == DIR_UP:
                l = "  ^  "
            elif lift_dir == DIR_DOWN:
                l = "  v  "
            else:
                l = "     "            
    else:
        l = "     "

    if floor == lift_floor:
        l = "|   |"

    print(f"{floor:^3}|{l}|{h}")

if building_parking:
    print("---|     |---")
    print(" P |     |   ")
    print("---|-----|---")
else:
    print("---|-----|---")


##########  RENDER FRAME  ##########
