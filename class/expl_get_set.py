# capsule = set/get
# content 0..100

class Box:

    def __getattr__(self, name):
        return f"you are trying to acces {name}"

    def __setattr__(self, name, value):
        print(f"you are trying to set {name}={value}")    

    # ------------------------------
    # |                            |
    # |                           <---- setter ("content")
    # |         value              |
    # |                         ----->getter ("content")
    # |                            |
    # ------------------------------

b1 = Box()

b1.content = -100
print(b1.content)



