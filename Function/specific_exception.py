from os import system

system("cls")

data = [ 10, 20, 30 ]

try:
    idx = int(input("Enter index: "))
    print( data[idx] )
except ValueError:
    print("Index can be only integer !!!")
except IndexError:
    print("The index was out of list range !!!")        