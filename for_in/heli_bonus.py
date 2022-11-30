from os import system
########
"""
se cere sa se marcheze (in baza coordonatelor hX,hY) si constructiilor conditionale, zona "periculoasa" din jurul aeroportului in asa maniera incat rezultatul sa arate astfel:

 BONUS! Sa presupunem ca trebuie sa marcam zona cu "zgomot sporit" in felul urmator

 1. # # # # # # # # # # 
 2. #     ~ ~ ~       # 
 3. #   ~ ~ ~ ~ ~     # 
 4. #   ~ ~ H ~ ~     # 
 5. #   ~ ~ ~ ~ ~     # 
 6. #     ~ ~ ~       # 
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

    map += str(f"{y + 1 :2}") + ". "  # numerotam rindurile 0-9 !!! numerotatia 1 la 10
    for x in range(SCALE):

        if x == 0 or x == SCALE - 1 or y == 0 or y == SCALE - 1:
            map += "# "

        elif x == hX and y == hY:
            map += "H "
        # # first task - middle
        elif x == hX - 2 and y == hY:
            map += "~ "
        elif x == hX - 1 and y == hY:
            map += "~ "
        elif x == hX + 1 and y == hY:
            map += "~ "
        elif x == hX + 2 and y == hY:
            map += "~ "
        # # second task - up - middle
        elif x == hX - 2 and y == hY - 1:
            map += "~ "
        elif x == hX - 1 and y == hY - 1:
            map += "~ "
        elif x == hX and y == hY - 1:
            map += "~ "
        elif x == hX + 1 and y == hY - 1:
            map += "~ "
        elif x == hX + 2 and y == hY - 1:
            map += "~ "
        # # next task - up - middle
        elif x == hX - 1 and y == hY - 2:
            map += "~ "
        elif x == hX and y == hY - 2:
            map += "~ "
        elif x == hX + 1 and y == hY - 2:
            map += "~ "

        # # third task - down - middle
        elif x == hX - 2 and y == hY + 1:
            map += "~ "
        elif x == hX - 1 and y == hY + 1:
            map += "~ "
        elif x == hX and y == hY + 1:
            map += "~ "
        elif x == hX + 1 and y == hY + 1:
            map += "~ "
        elif x == hX + 2 and y == hY + 1:
            map += "~ "
            # # next task - up - middle
        elif x == hX - 1 and y == hY + 2:
            map += "~ "
        elif x == hX and y == hY + 2:
            map += "~ "
        elif x == hX + 1 and y == hY + 2:
            map += "~ "
        # mision done,

        else:
            map += "  "

    map += "\n"

print(map)
