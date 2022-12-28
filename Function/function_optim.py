""""

Functii. Optimizarea codului utilizand functiile
Signatura functiei sau prototipul acesteia, reprezinta informatia generala cunoscuta despre ea. Cel mai des prototipul reprezinta "formula" care indica tipul returnat, denumirea, tipurile si denumirile argumentilor.

Sa se declare o functie care corespunde urmatorului prototip
drawLine( length, direction )
astfel incat, atunci cand vom executa codul:
drawLine( 5, 'h' )
rezultatul sa fie
-----
iar atunci cand vom executa codul:
drawLine( 3, 'v' )
rezultatul sa fie
|
|
|

"""
from os import system

system("cls")

def drawLine( length, direction ):
    direction = "-"
    print(length * direction)

drawLine( 5, "h")

def drawLine(length, direction):
    direction = "|\n" 
    print(length * direction)

drawLine( 3, "v")    
