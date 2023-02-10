from os import system

system('cls')

student = {'name':'Elizabet', 'age':28, 'courses':['Math', 'CompSci']}

print(student['courses'][1]) # extract exact

student['phone'] = '555-65965'

print(student.get('phone', 'Not Found')) # if not key will receve Not Found

student['name'] = 'Vitaly'

student.update({'name':'Johanes', 'age':21, 'phone': '222-3325'}) # change a dict

print('1 -', student.keys())    # extract key
print('2 -', student.values()) # extract only value
print('3 -', student.items())

print('#'*40)
for key, value in student.items():
    print(key, value)

########### remove ##############

#del student['age'] # remove all  

age = student.pop('age') # remove only key, not value!!

print(student)
print(age)