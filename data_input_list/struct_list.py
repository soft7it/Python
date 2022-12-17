# Python DATA STRUCTURES:
#  list = ordered collection / array
#  1. indexed
#  2. dynamic
#  3. typefree ( hint: recomended - same type)
# 
#   + iteration
# 

#################################################
temps  = [ 10.0,  9.0,  8.0,  0.0, -5.0, -10.0,  0.0 ]
days   = [ "Mo", "Tu", "Wd", "Th", "Fr", "Sat", "Sun"]
# index       0,   1,   2

for i in range( 7 ):
    if temps[i] <= 0:
        sign = "*"
    else:
        sign = " "    
        
    print( sign, days[i], temps[i] )

for t in temps:
    print( t )