# capsule = set/get
# content 0..100

class Box:

    def __getattr__(self, name):
        if name == "content":
            return self.__dict__[name]

    def __setattr__( self, name, value ):
        if name == "content" and value >= 0 and value <= 100:
            self.__dict__[name] = value
        else:
            print("Wrong attribute or value")   

    # ------------------------------
    # |                            |            
    # |                           <---- setter ("content")            
    # |         .__dict__          |             
    # |             [name]       ----->getter ("content")
    # |                            |          
    # ------------------------------             

b1 = Box()

b1.content = 1
b1.x = -100  # acesta da eroarre
print(b1.content)
