class Employe:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def payroll(self):
        return ('Salarry gross {0}'.format(self.pay) + ' and netto {0}'.format(self.pay) + f' - {24}%')

emp_1 =Employe('Andy', 'Jesy', 50000)        
emp_2 =Employe('Boris', 'Jonson', 60000)

emp_1.fullname()
print(Employe.fullname(emp_1))

print(emp_2.fullname())
print(emp_2.payroll())