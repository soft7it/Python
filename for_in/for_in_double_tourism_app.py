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

for i in destination:
    system("cls")
    print("EU :" + "\n" + "   -" + destination[0][0]
                 + "\n" + "   -" + destination[0][1]
                 + "\n" + "   -" + destination[0][2]
                 + "\n" + "   -" + destination[0][3]
                 + "\n" + "   -" + destination[0][4]
    + "\n" + "US :" + "\n" + "   -" + destination[1][0]
                 + "\n" + "   -" + destination[1][1]
                 + "\n" + "   -" + destination[1][2]
                 + "\n" + "   -" + destination[1][3]
                 + "\n" + "   -" + destination[1][4])
