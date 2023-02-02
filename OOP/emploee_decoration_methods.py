class Employe:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property   
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)   

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!') # verificam conditia executata

# atentie la __init__ cite argumente are, altfel error
emp_1 = Employe('Andy', 'Jesy')
emp_2 = Employe('Boris', 'Jonson')

emp_1.fullname = 'Cornelius Bezzos'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname