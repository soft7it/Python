# Private members
# OOP - encapsulation

class Box:

    def __init__(self, content):
        if content != None:
            self.__content = content
        else:
            print("Error! Non cannot be in tne Box")    
        
    def __str__(self):
        return f"Box [{self.__content}]"

######################################################
# 

b1 = Box("A good Book")
b2 = Box("A Music disc")

b1.__content = None

print(b1)
print(b2)