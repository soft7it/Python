# Save structure to -> Json file

from json import dumps # library special for save data structure

# data structure (Python)
person = {
    "name": "John",
    "age": 30,
    "alive": True,
    "interests":[       # formam o lista in dictionar json
        "programing",
        "hacking"
    ]
}

# save the data
file = open("person.json","w")
file.write( dumps(person) ) # dictionar
file.close()