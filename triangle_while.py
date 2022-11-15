from os import system
# draw this triangle
# HW1:  size from keyboard 
#       +
#      +++
#     +++++

system("cls")


# print("..+")    # 2/1
# print("..+")    # 1/3
# print("..+")    # 0/5

#m = int(input("you number : "))

n = 0
while n < 3:
    print(" "*(2-n), "+"*(2*n+1))
    n += 1


############################
num = int(input("you number : "))
n = 0
while n < num:  
    if num % 2 == 0: # numere pare
        print(" "*(num-n), "+"*(num*n))
        num += 1
    else: # numere impare
        print(" "*(num-n), "+"*(2*n+1))
        n += 1

