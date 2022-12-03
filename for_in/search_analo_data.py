
items = ["Marry", "Peter"]  # this is what we search for in !!!
found = [ False,  False ]

container = [ "John", "Marry", "Bob"]  # where to look for
# index           0,        1,    2


for j in range( len(items) ):

    for i in range( len(container) ):
        found[j]  = container[i] == items[j]  # bool ( True \ False) < remember
        if found[j]:
            break


########################################
print(items)
print(found)
for j in range( len(items) ):
    if found[j]:                        # CHECK THE MEMORRY
        print(items[j], "FOUND") 
    else:
        print(items[j], "NOT FOUND")           