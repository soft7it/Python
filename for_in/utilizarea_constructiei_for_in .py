from os import system
# Avem la dispozitie urmatorul cod:
"""
rezultatul executarii caruia este:

# . . . . . . . . . 
# . . . . . . . . . 
# . . . . . . . . . 
# . . . . . . . . . 
# . . . . . . . . . 
# . . . . . . . . . 
# . . . . . . . . . 
# . . . . . . . . . 
# . . . . . . . . . 
# . . . . . . . . .
"""

"""
SE CERE:
Sa se adauge conditiile potrivite in if astfel incat rezultatul sa devina:
# # # # # # # # # # 
# . . . . . . . . # 
# . . . . . . . . # 
# . . . . . . . . # 
# . . . . . . . . # 
# . . . . . . . . # 
# . . . . . . . . # 
# . . . . . . . . # 
# . . . . . . . . # 
# # # # # # # # # # 
"""
system("cls")
print("\n")

for y in range(1, 11):
    
    for x in range(1, 11):        
        if x == 1:
            print("#", end=" ")
        elif x == 10:
            print("#", end=" ")
        elif y == 1:
            print("#", end=" ")
        elif y == 10:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()

print("\n")
