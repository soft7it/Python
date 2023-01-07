name = input("Enter your name please: ")

## Save it to a file  ####

file = open("name.txt","w") # w - > writing
file.write(name)
file.close()