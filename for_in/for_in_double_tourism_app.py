from os import system

# bidimensional / 2 level

destination = [
    [
        "London",
        "Dublin",
        "Paris",
        "Amsterdam",
        "Wien",
    ],
    [
        "New York",
        "San Diego",
        "Washington",
        "Chicago",
        "Kansas",
    ]
]
system("cls")

print(f"EU: ")
for i in destination[0]:     
    
    print("   - " + i)

print(f"US: ")
for us in destination[1]:

    print("   - " + us)
