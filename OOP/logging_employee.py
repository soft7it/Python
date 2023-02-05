import logging

logging.basicConfig( filename='employe.log', level=logging.INFO,
                    format='%(asctime)s:%(lavelname)s:%(message)s')

## LogRecord attributes

class Employe:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employe('Andy', 'Jesy')        
emp_2 = Employe('Boris', 'Jonson')
emp_3 = Employe('Vitaly', 'Boss')