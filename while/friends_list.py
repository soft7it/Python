# Fact: list of friends

# empty list

friends = []

while len( friends ) < 100:
    name = input("Add friend name: ")
    if name == "":
        break
    # HW : check if the name is in the list
    #   operator in
    if name in friends:
        print("You have already this friend name " + name)
        break
    friends.append( name )

print("You have", len( friends ), "friends")
for i in range( len(friends) ):
    print(" ",i,">>",friends[i])  
