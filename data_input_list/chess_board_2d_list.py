from os import system

# tuple / constant list
SIZE = (8,8)
#       ^
#      [0]

BKING = 1
BQUEEN = 2
BBSHOP = 3
BKNIGHT = 4
BROOK = 5
BPAWN = 6

# list 2demensional
board = [
    [ 5, 4, 3, 1, 2, 3, 4, 5 ],
    [ 6, 6, 6, 6, 6, 6, 6, 6 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
]

alfabet = "abcdefgh"

###########  PRINT BOARD ###############
system("cls")

for alf in alfabet:
    print("   " + alf[0] + " ", end="")

print()    
    
#     print(f"   " + alf + " ", end="")
# print()

# HW : display horizontal coordinates abcdefgh
#       using a separate loop here

for ri in range(SIZE[0]): # coordonatele iese de la 0 la 7 
    rc = SIZE[1] - ri     # intoarcem coordonatele de la 8 la 1
    print(" " + "-----"*SIZE[1]) # face rindurile de sus a celulei
    print(rc, end="")

    for ci in range(SIZE[1]): # afiseaza rindurile pe verticala
        piece = " "
        if board[ri][ci] == BKING:  
            piece = "♚"   # https://www.utf8icons.com/search?query=chess
        elif board[ri][ci] == BQUEEN:  
            piece = "♕"   
        elif board[ri][ci] == BBSHOP:  
            piece = "♗"   
        elif board[ri][ci] == BKNIGHT:  
            piece = "♘"   
        elif board[ri][ci] == BROOK:  
            piece = "♖"   
        elif board[ri][ci] == BPAWN:  
            piece = "♟"
        print(f"| {piece}  ", end="")    # dpa piece spatiu 2!!
    
    print(f"|{rc}") # afisham ultima bara a coloanei 8
    

print(" " + "-----"*SIZE[1])   # afisham partea de jos din fiecare celula din coloana 

for alf in alfabet:
    print("   " + alf[0] + " ", end="")
