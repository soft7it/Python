# Draws triangles

#            p  h  s
#   + + *    2  1  1
#   +  ***   1  2  3
#     *****  0  3  5

#    *******    4  7


def triangle( h, o ) :
    s = 1
    p = h - 1 # p = 3 - 1 solutionam distanta din stinga
    for r in range(h):
        if h == 3 :
            o = 6
        elif h == 5 :
            s = 3
            h = 6
            o = 3
        elif h == 7:            
            s = 5
            h = 4
        print( "  " * o + "  " * p + "* " * s )
        s += 2
        p -= 1
        
        
#######################
triangle(3, 4)        
triangle(5, 2)        
triangle(7, 0)   

# HW : try to modify the function so it skips a few rows,
#  use if + ignore print 

#### Test done ######
