from os import system
from time import sleep

# add content
ads = [
    "Buy this Python course book for only 0.99$",
    "Try this course of Python for free!!!",
    "Drink a lot of water (2L per day minim)",
]

# Metod 1 : index only

while True:
    ad = ads.pop(0)
    system("cls")
    print(" >> ", ad , " << ")
    sleep(3)
    
    ads.append(ad)
