# Load structure to < - Json file

from json import loads # librery for load data from file

# data structure (Python)

# save the data
file = open("person.json","r")
person = loads( file.read() ) # read as a Json

print(person["interest"][0])
