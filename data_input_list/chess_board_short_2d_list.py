from os import system

## CHESS BOARD + PIECES

#   * list 2d / matrix
#   * loops and conditionals
#   * algorithms

# tuple / constant list

SIZE = (8,8)

EMPTY = 0

BKING = 1
BQUEEN = 2
BBSHOP = 3
BKNIGHT = 4
BROOK = 5
BPAWN = 6

WKING = 11
WQUEEN = 12
WBSHOP = 13
WKNIGHT = 14
WROOK = 15
WPAWN = 16

# LIST 2D- DEMISIONAL
board = [
    [  5,  4,  3,  1,  2,  3,  4,  5 ],
    [  6,  6,  6,  6,  6,  6,  6,  6 ],
    [  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0 ],
    [ 16, 16, 16, 16, 16, 16, 16, 16 ],
    [ 15, 14, 13, 11, 12, 13, 14, 15 ],
]

pieces = " ♚♛♝♞♜♟    ♔♕♗♘♖♙"
# index   0 1 2 ....      ^
#                         11 index
pieces_codes = [" ", "wk", "wq", "wb", "wn", "wr", "wp", ] # ,     "bk", "bq", "bb", "bn", "br", "bp"
# index           0,   1,    2,   3,     4,    5,    6

alfabet = "abcdefgh"

white_score = 0

game_over = False
while not game_over:

    ####################### PRINT BOARD #################
    system("cls")
    print(" ", end="")
    for c in alfabet:
        print(f"{c:^5}", end="")

    print()

    for ri in range( SIZE[0] ):
        rc = SIZE[1] - ri
        print( " " + "-----"*SIZE[1])
        print(rc, end="")

        for ci in range( SIZE[1] ):
            piece = pieces[ board[ri][ci] ]
            print(f"| {piece}  ", end="")

        print("|")

    print(" " + "-----"*SIZE[1])
    ###################  PRINT BOARD  ############### 

    ################### INTERACTION ##################
    move = input("your move > ")
    #  {fig}{from}{to}
    #  wpd2d3 - white pion din d2 mutate la d3
    what_, from_, to_ = move[0:2], move[2:4], move[4:6]
    if what_ not in pieces_codes or what_ == " ":
        print("The figure you try to move does not exist.")
    else:
        piece_code  = pieces_codes.index(what_)
        ri_from     = SIZE[0] - int(from_[1]) # 8 - 2 = 6 (move is 2,3)
        ci_from     = alfabet.index(from_[0])
        
        ri_to     = SIZE[0] - int(to_[1])
        ci_to     = alfabet.index(to_[0])

        if board[ri_from][ci_from] == piece_code:
            if piece_code == WPAWN:
                if ci_from == ci_to: # daca este pe aceeasi coloana deplasarea
                    if ri_to - ri_from == 1 or\
                        ri_to - ri_from == 2 and ri_from == 1:
                        #print("!")  # controlom debuging
                        if board[ri_from][ci_from] == EMPTY: # daca matricia este goala atunci paseste pe urmatoarea
                            board[ri_from][ci_from] = EMPTY # il scoatem si ilocuim cu zero -gol
                            board[ri_to][ci_to] = piece_code
                # elif bataia fifurei            


        # print(what_, from_, to_) # 3printuri decodarea coordonatelor
        # print(ri_from, ci_from)
        # print(ri_to, ci_to)
        input()      
    ################### INTERACTION ################## 
    #  HW: 
    #   1. check left / right diagonals      17:00 min video!!!
    #   2. check it the is a piece
    #   3. increase the score by corresponding value