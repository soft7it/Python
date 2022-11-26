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

    map += str(y + 1) + ". " # numerotam rindurile 0-9 !!! numerotatia 1 la 10
    for x in range(SCALE):

        if x == 0 or x == SCALE -1 or y == 0 or y == SCALE - 1:
            map += "# "

        elif x == hX and y == hY:
            map += "H "
        # # first task - midle
        elif x == hX - 2 and y ==  hY :
            map += "F "
        elif x == hX - 1 and y ==  hY :
            map += "F "
        elif x == hX + 1 and y ==  hY :
            map += "F "
        elif x == hX + 2 and y ==  hY :
            map += "F "
        # # second task - up
        elif x == hX - 1 and y ==  hY - 1:
            map += "F "
        elif x == hX  and y ==  hY - 1:
            map += "F "
        elif x == hX + 1 and y ==  hY - 1:
            map += "F "
        # # third task - down
        elif x == hX - 1 and y ==  hY + 1:
            map += "F "
        elif x == hX  and y ==  hY + 1:
            map += "F "
        elif x == hX + 1 and y ==  hY + 1:
            map += "F "
        ## mision done,             
            
        else:
            map += "  "

    map += "\n"

print(map)
