## keyword - class: schema, type, template,...
#          - function -> factory
# #############################################
#  1. Step - define
class Dog:
    def __init__(self):
        print("Init was called!!!")
        #self.race = "hakedrace" # Am adaugato noi fara liste de date

def createDog(name, race, year, alive):
    dog = Dog()  # dog <<< +race
    dog.name = name
    dog.race = race
    dog.year = year
    dog.alive = alive
    return dog
    
def printDog(dog):
    print(dog.name)
    print(dog.race)
    print(dog.year)
    print(dog.alive)
    
# 2. Step - use
my_dog = createDog("Tizik","BullDog",2010,True)
printDog(my_dog) ## atentie chemi functia

# friends_dog = createDog("Sharik", "Pitbul", 2018, True)
# printDog(friends_dog)    