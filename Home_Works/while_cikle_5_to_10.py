from os import system

"""
Se cere sa se:
    - Citeasca de la tastatura doua variabile start_n si end_n
    - Sa se modifice codul de mai sus in asa mod incat daca utilizatorul
     introduce prima valoare mai mica si cea de a doua mai mare(de ex: 5 si 10) ciclul
     sa afiseze toate valorile in ordine crescatoare de la 5 la 10, iar daca valorile 
     se introduc invers(de ex: 10 si 5) sa se afiseze toate numerele intregi
     in ordine descrescatoare din acest diapazon
    - Utilizati if / else pentru a solutiona acest exemplu
"""

system("cls")

start_n = int(input("you number A: "))
end_n = int(input("you number B: "))

increase = 10
decrease = 1

if start_n <= end_n and end_n <= 10:
    while start_n <= end_n:
        print(start_n)
        start_n += 1
        if start_n > increase:
            break
else:
    while start_n >= end_n and start_n <= 10:
        print(start_n)
        start_n -= 1
        if start_n < decrease:
            break
#########################  test DONE !!! ####################   
