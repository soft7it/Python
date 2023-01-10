from json import loads
from os import system

# Load from file
def loadFood():
    file = open("data/food.json", "r")
    food = loads(file.read())
    # print(type(food))  # poti testa sa vezi ce tipuri de date ai -lista
    return food

# print the meniu

def printFood(food):
    system("cls")
    print("#"*50)
    for i in range(len(food)):
        print(
            f"{i+1}) {food[i]['name']:20} {food[i]['price']['amount']:8.2f} {food[i]['price']['currency']}")
    print("#"*50)
### option  ######
def printMeniu():
    system("cls")
    print("#"*50)
    print("1. Show menu")
    print("2. Add to order")
    print("0. Exit")
    print("#"*50)
    option = int(input(">>> "))
    return option