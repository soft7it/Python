from os import system
# user input word
# determine if it's a int, float. str

system("cls")

value = input("Enter a word : ")

try:
    n = int(value)
    print(f"{n} is an INTEGER.")
except:
    try:
        n = float(value)
        print(f"{n} is a FLOAT.")
    except:
        print(f"{value} is a STRING.")        