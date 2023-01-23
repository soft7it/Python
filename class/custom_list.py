## Custom Container / List

##  ! DO NOT USE LIST/DICTS/TUPLES/SETS  
##  - hold up to 3 numeric values
##  - allow only float or int
##  - operate with [], .append, .remove[]

from time import sleep

class NumberContainer:
    # initialization / constructor
    def __init__(self):
        self.val0 = None
        self.val1 = None
        self.val2 = None

    # HW: add type check to any SETTING method
    #     if type is not float or int
    #     throw TypeError

    def append(self, value):
        if self.val0 == None:
            self.val0 = value    
        elif self.val1 == None:
            self.val1 = value    
        elif self.val2 == None:
            self.val2 = value

    def __getitem__(self, key):
        if key == 0:
            return self.val0            
        elif key == 1:
            return self.val1            
        elif key == 2:
            return self.val2

    def __setitem__(self, key, value):
        if key == 0:
            self.val0 = value
        elif key == 1:
            self.val1 = value
        elif key == 2:
            self.val2 = value

    def __len__(self):
        length = 0
        if self.val0 != None:
            length = 1
        if self.val1 != None:
            length = 2
        if self.val2 != None:
            length = 3
        return length        
        
 # make it iterable
    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        value = self[self.idx] # in containere separate value sunt diferite si nu intra in conflict cu altele conanire numite aceeasi valoare
        if value == None:
            raise StopIteration # opreste iteratia ---> signal For to stop
        self.idx += 1
        return value
    
# HW : add method .remove(idx) 
#   delete  the value from that call
#   10 20 30   
#       ^  video 30:00 min  

"""
    get / set
OBJ --------> ext
    <------
"""


#################################
nc = NumberContainer()
nc.append(10)
nc.append(20)
nc.append(30)

# print( len[nc] )

# print( nc[0] )
# print( nc[1] )
# print( nc[2] )

# for i in range( len(nc) ):
#     print( nc[i] )

for v in nc:
    print(v)
    sleep(3)

"""
1. for ----> ? iter(nc)
       <---- nc
2. each step 
        ----> next(nc)       
"""