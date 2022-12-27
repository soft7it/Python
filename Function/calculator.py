def ii( which ):
    print("Enter",which, "integer: ", end="")
    return int(input())

a = ii("first")    
b = ii("second")

op = input("Choose oeration (* / + -): ")  # op = "+" adica egala cu valoarea care intra

res = 0

# HW : next operations: /  - **, if the user choses an inexistent operations
# -> "wrong operation"

if op == "+":
    res = a + b
elif op == "*":
    res = a * b
elif op == "/":
    res = a / b
elif op == "-":
    res = a - b
elif op == "**":
    res = a ** b
else:
    print("you choosed an inexistent operations")        

print("Result: ", res)     