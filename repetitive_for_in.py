from os import system

# Avem la dispozitie un cod care deseneaza harta locurilor unei parcari
#  automatizate cu un numar de locuri total predefinit si un singur loc liber
"""
#########################################
| X | | X | | X | | X | | X | | X | | X |
#########################################
"""
"""
SE CERE:

        Sa se adauge o conditie prin if .. else ... in interiorul ciclului astfel
        incat rezultatul sa reflecte si locul liber:

        ###################################
        | X || X ||   || X || X || X || X |
        ###################################

        Sa se raspunda la intrebarea: - ce reprezinta parametrul sep in functia print()
        si de ce a fost nevoie de acesta ?
"""

system("cls")

PARKING_PLACES = 7
FREE_PLACE = 3
# newList = []

# desnam rindul de sus x>###
print("#"*PARKING_PLACES*5)
## ciklu xxx
for place_index in range(1, PARKING_PLACES + 1):
    if place_index == FREE_PLACE: continue
    #print("|  |", end="")
        #break
    #print(place_index)
    print("| X |", end="")
        
    #FREE_PLACE in range(place_index):   
       #continue
    # print("| X |", end="")
     #FREE_PLACE == place_index(FREE_PLACE):
    #
    #if newList.append(3):
    # if place_index.index(FREE_PLACE): #range(3): #place_index.pop(3):
        # break
        # print("| X |", end="")
        # break
# else:
#     print("| X |", end="")
## desenam rindul de jos
print("\n", "#"*PARKING_PLACES*5, sep="")











# Parametru sep="" - formateaza ordene si adauga ce si cum comenzi in print ordenea sau separarea, exemplu:
    
# for formatting a date
# print('09','12','2016', sep='-')

# rezultatul va fi:
# 09-12-2016