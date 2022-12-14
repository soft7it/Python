from os import system
from time import sleep

# add content
ads = [
    "Buy this Python course book for only 0.99$",
    "Try this course of Python for free!!!",
    "Drink a lot of water (2L per day minim)",
]

# Metod 1 : index only
index = 0
while True:
    system("cls")
    print(" >> ", ads[index], " << ")
    sleep(3)
    index += 1
    if index >= len(ads):
        index = 0