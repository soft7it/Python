from os import system
from random import randint

system("cls")

# Parse string

# Moldova, Chisinau, str. Eminesci 123

# aviable countries: Romania, Moldova
# Slut, Noroc
# 1. data input
data = input("enter address: ")
fragments = data.split(",")
print(fragments)

# 2. separate / multiple assigment
country, city, street = fragments

# 3. clean data (curatam spatiile sin prejur)
country = country.strip()
city = city.strip()

# chaining# replace - curata datele din stinga si pune curat
street, number = street\
                    .strip()\
                    .replace("str. ", "")\
                    .split(" ")
number = int(number)  # "123" == 123 transformam in numar                  

# PROMOTION
if randint(122,124) == number:
    if number > 100: 
        print("!!! You won £ 1.000.000 !!!")                   
