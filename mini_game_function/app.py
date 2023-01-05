from map import *
from ui import *
# from os import rmdir
# rmdir("C:\Users\soft7\OneDrive\Documents\Python_lesson\Test_python_HW\mini_game_function\__pycache__")

while True: 
    clear()
    printMap( gameMap )
    key = controls()
    

    if key == 'x':  # tasta iese din jok
        break        
    
    if rc <= 8:       
        if key == "d" and gameMap[rr][rc+1] != 3 or key == "d" and gameMap[rr][rc+2] != 3: # :
            print("WARNING DANGER!!!")
            input()
            if key == "d" and gameMap[rr][rc+1] != 1: # directia spre dreapta cu conditia daca se misca cu +1 nu intilneste 1
                    
                gameMap[rr][rc] = 0 # erase the robot
                rc += 1             # increment coord
                gameMap[rr][rc] = 2

    if 0 < rc :
        if key == "a" and gameMap[rr][rc-1] != 1:  # directia spre stinga
            gameMap[rr][rc] = 0  # erase the robot
            rc -= 1             # decrement coord
            gameMap[rr][rc] = 2  # punem robotul la lok

    # HW: add Up/Down movement 
    # : bondaries check right -> 9, left - 0 stop
    # : map add same dange mark X, in the moment you move you have radar position rc+1, rc+2 not mine   
    # in casa od danger -> WARNING -> danger detection
    
    # if key == "s" and gameMap[rr+1][rc] != 1: # directia spre jos
    #     if rr < 9:
    #         rr += 1
    #         gameMap[rr][rc] = 2
        
    # if key == "w" and gameMap[rr-1][rc] != 1: # directia spre sus
    #     if 0 < rr:
    #         rr -=1
    #         gameMap[rr][rc] = 2
