from map import *
from ui import *
from radar import *

while True: #rc != 9 or rc != 0 or rr != 9 or rr != 0:  #
    clear()
    printMap( gameMap )
    key = controls()
    

    if key == 'x':  # tasta iese din jok
        break

    gameMap[rr][rc] = 0 # erase the robot
    
    if key == "d" and gameMap[rr][rc+1] != 1: # directia spre dreapta cu conditia daca se misca cu +1 nu intilneste 1
        if rc == 9:
            break
        else:
            rc += 1             # increment coord
            gameMap[rr][rc] = 2

    if key == "a" and gameMap[rr][rc-1] != 1:  # directia spre stinga
        if rc != 0:
            rc -= 1             # decrement coord
            gameMap[rr][rc] = 2  # punem robotul la lok

    # HW: add Up/Down movement 
    # : bondaries check right -> 9, left - 0 stop
    # : map add same dange mark X, in the moment you move you have radar position rc+1, rc+2 not mine   
    # in casa od danger -> WARNING -> danger detection
    if key == "s" and gameMap[rr+1][rc] != 1: # directia spre jos
        if rr != 9:
            rr += 1
            gameMap[rr][rc] = 2
    if key == "w" and gameMap[rr-1][rc] != 1: # directia spre sus
        if rr != 0:
            rr -=1
            gameMap[rr][rc] = 2
