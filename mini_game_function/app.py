from map import *
from ui import *
# from os import rmdir
# rmdir("C:\Users\soft7\OneDrive\Documents\Python_lesson\Test_python_HW\mini_game_function\__pycache__")

MAX_ROWS = len(gameMap)  # MERGE JOS
MAX_COLS = len(gameMap[0]) # MERGE PE ORIZONTALA - > dreapta


while True: 
    clear()
    printMap( gameMap )
    key = controls()
    ######################################################################
    if key == 'x':  # tasta iese din jok
        break
        
    # directia spre dreapta cu conditia daca se misca cu +1 nu intilneste 1       
    ####################  right ############################################
    if key == "d" and rc < MAX_COLS - 1: # 2 < 10-1 == 9
        if gameMap[rr][rc+1] != 1:            
            gameMap[rr][rc] = 0  # erase the robot
            rc += 1             # increment coord
            gameMap[rr][rc] = 2
            if rc < MAX_COLS - 2: # 2 < 10 - 2, # findca 8/ rc-7+2?? 
                if gameMap[rr][rc+2] == 3 or gameMap[rr][rc+1] == 3:
                    print("WARNING DANGER!!!")
                    input(">>")         
                 
    if key == "a" and 0 < rc:
        if gameMap[rr][rc-1] != 1:  # directia spre stinga
            gameMap[rr][rc] = 0  # erase the robot
            rc -= 1             # decrement coord
            gameMap[rr][rc] = 2  # punem robotul la lok
            if rc > 0:
                if gameMap[rr][rc-2] == 3 or gameMap[rc][rc-1] == 3:
                    print("WARNING DANGER!!!")
                    input(">>")
    ###################### left ###################################
   
       # HW: add Up/Down movement 
    # : bondaries check right -> 9, left - 0 stop
    # : map add same dange mark X, in the moment you move you have radar position rc+1, rc+2 not mine   
    # in casa od danger -> WARNING -> danger detection
    if key == "s" and  rr < MAX_ROWS - 1: # 3 < 10-1 == 9 rc +1
        if gameMap[rr+1][rc] != 1: # directia spre jos
            gameMap[rr][rc] = 0  # erase the robot
            rr += 1
            gameMap[rr][rc] = 2
            if rr < MAX_ROWS - 2:
                if gameMap[rr+2][rc] == 3 or gameMap[rr+1][rc] == 3:
                    print("WARNING DANGER!!!")
                    input(">>")
    ###################  down  ######################################              
    if key == "w" and 0 < rr:    
        if gameMap[rr-1][rc] != 1: # directia spre sus
            gameMap[rr][rc] = 0  # erase the robot
            rr -= 1
            gameMap[rr][rc] = 2
            if rr > 2:
                if gameMap[rr-2][rc] == 3 or gameMap[rr-1][rc] == 3:
                    print("WARNING DANGER!!!")
                    input(">>")
    ######################  UP  ###################################  
