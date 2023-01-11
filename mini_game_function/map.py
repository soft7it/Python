# this Module contains the MAP logic
#
# GAME MAP - matrix
# 0 - empty
# 1 - wall
# 2 - robot
# 3 - trap(mine)

rr = 4
rc = 2
gameMap = [
    [0,0,0,0,0,0,0,0,0,0],  # rindul 0
    [0,0,3,0,0,0,0,0,3,0],  # rindul 1
    [0,1,0,1,0,0,0,0,0,0],  # rindul 2
    [0,0,0,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,3,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,0,3,0,0,0,1,0,0,0],
    [0,3,0,0,3,0,0,0,3,0],
    [0,0,0,0,0,0,0,0,0,0],  # rindul 9
  # celula 0,1,2......,9 
]

gameMap[rr][rc] = 2  # put the robot in specifiet cordonation

def p( c ):
    print(c + " ", end="")

def printMap( m ):
    for ri in range(10):
        for ci in range(10):

            # p(".") if m[ri][ci] == 0: else None - sintaxa python des intilnita!!!!!
            if m[ri][ci] == 0:
                p(".")
                # print(". ",end="") ## formeaza functia de sus p
            if m[ri][ci] == 1:
                p("#")
                # print("# ",end="") ## formeaza functia de sus p
            if m[ri][ci] == 2:
                p("R")
            if m[ri][ci] == 3:
                p("X")    

        print()

if __name__ == "__main__":
    print(len(gameMap))
    print(len(gameMap[0]))
