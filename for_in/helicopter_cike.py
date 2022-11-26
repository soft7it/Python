from os import system
########
"""
se cere sa se marcheze (in baza coordonatelor hX,hY) si constructiilor conditionale, zona "periculoasa" din jurul aeroportului in asa maniera incat rezultatul sa arate astfel:

 1. # # # # # # # # # # 
 2. #                 # 
 3. #     x x x       # 
 4. #   x x H x x     # 
 5. #     x x x       # 
 6. #                 # 
 7. #                 # 
 8. #                 # 
 9. #                 # 
10. # # # # # # # # # # 

"""
SCALE = 10

hX = 4
hY = 3

map = ""
for y in range(SCALE):
    system("cls")

    if y <= 8:
        map += " " + str( + y + 1) + ". " # numerotam rindurile 0-9 !!! numerotatia 1 la 10
    else:
        map += str(y + 1) + ". " 
    for x in range(SCALE):

        if x == 0 or x == SCALE -1 or y == 0 or y == SCALE - 1:
            map += "# "

        elif x == hX and y == hY:
            map += "H "
        # # first task - midle
        elif x == hX - 2 and y ==  hY :
            map += "x "
        elif x == hX - 1 and y ==  hY :
            map += "x "
        elif x == hX + 1 and y ==  hY :
            map += "x "
        elif x == hX + 2 and y ==  hY :
            map += "x "
        # # second task - up
        elif x == hX - 1 and y ==  hY - 1:
            map += "x "
        elif x == hX  and y ==  hY - 1:
            map += "x "
        elif x == hX + 1 and y ==  hY - 1:
            map += "x "
        # # third task - down
        elif x == hX - 1 and y ==  hY + 1:
            map += "x "
        elif x == hX  and y ==  hY + 1:
            map += "x "
        elif x == hX + 1 and y ==  hY + 1:
            map += "x "
        ## mision done,             
            
        else:
            map += "  "

    map += "\n"

print(map)
