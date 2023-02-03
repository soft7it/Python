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
        # return ('Salarry gross {0}'.format(self.pay) + ' and netto {0}'.format(self.pay) + f' - {24}%')
        return (f'Salarry gross {self.pay} and netto {self.pay*0.76}')
    
class Developer(Employe):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employe):
    raise_amt = 1.40

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.emploees = []
        else:
            self.emploees = employees

    def add_emp(self, emp):
        if emp not in self.emploees:
            self.emploees.append(emp)

    def remove_emp(self, emp):
        if emp in self.emploees:
            self.emploees.remove(emp) 

    def print_emps(self):
        for emp in self.emploees:
            print('-->', emp.fullname())                   

dev_1 = Developer('Andy', 'Jesy', 50000, 'Python')
dev_2 = Developer('Boris', 'Jonson', 60000, 'Java')

mgr_1 = Manager('Simon', 'Lee', 90000, [dev_1])

print(mgr_1.pay)

mgr_1.add_emp(dev_2)  # adauga data
mgr_1.remove_emp(dev_1) # elimina data

mgr_1.print_emps()

print(issubclass(Manager, Developer))
print(isinstance(mgr_1, Developer))

# print(dev_1.pay)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

