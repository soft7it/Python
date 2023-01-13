gameMap = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

coord = [0]

# Algo -> save the map
# manual serialization
# ALGO < load map from file
def saveMap( m, c ):
    file = open("map.txt", "w")
    # salveaza fisieru
    for ri in range(3):
        for ci in range(3):
            file.write(str(m[ri][ci]))
    file.write(str(c[0])) # la sfirsit scriemi coodonata ca string

    file.close()

def loadMap( m, c ):
    file = open("map.txt", "r")
    # incarca fisieru
    for ri in range(3):
        for ci in range(3):
           m[ri][ci] = int( file.read(1) ) # le citeste ca str si trebuie convertite in int
    c[0] = int(file.read(1))
    file.close()

# list methods
def printMap( m, c ):
    # afisarea
    for ri in range(3):
        for ci in range(3):
            print(str(m[ri][ci]), end="")

        print()
    print( c[0] )        

#################################################################
# 1.
# saveMap(gameMap, coord)
# # 2.
loadMap(gameMap, coord)
printMap(gameMap, coord)  

# hw: add save  load into the game video 15:30
