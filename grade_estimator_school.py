from os import system
# IN: student`s grade 1 to 10
# OUT: good, ok, bad

# x ----> x -----> x -----> x
# 1       4        7        10


grade = int(input(" You grade: "))

system("cls")

if grade > 7 and grade <= 10:
    print("GOOD!")
elif grade > 4 and grade <=7:
    print("OK!")
elif grade >= 1 and grade <=4:
    print("BAD!") 
elif grade <= 0:
# or grade < 10:
    print("Value is wrong")
else:
    print("Value is wrong")
      

# HW3: continiue with -Wrong Value       