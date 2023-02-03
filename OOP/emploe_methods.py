class Employe:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employe.num_of_emps += 1  # aratatam citi angajati avem

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def payroll(self):
        return (f'Salarry gross {self.pay} and netto {self.pay*0.76}') # extract 24% from salarry
    
    def __repr__(self):
        return ("Employee ('{}','{}','{}')".format(self.first, self.last, self.pay))
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other): # adaugam sumam salarry
        return self.pay + other.pay
    
    def __len__(self):  # determinam mumarul de date din cuvint => data
        return len(self.fullname())
    

emp_1 = Employe('Andy', 'Jesy', 50000) # atentie la __init__ cite argumente are, altfel error
emp_2 = Employe('Boris', 'Jonson', 60000)

# print(emp_1)

# print(repr(emp_1))    # adauga datele din lista care le cerem
# print(str(emp_1))

# print(emp_1.__repr__) # adauga datele din lista care le cerem
# print(emp_1.__str__)

# print(emp_1 + emp_2) # salariul total a muncitorilor

print(len(emp_1)) # verificam numarul de date 