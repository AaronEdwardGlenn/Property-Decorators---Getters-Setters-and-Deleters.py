# lets review property decorators:


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Aaron', 'Glenn', 1000)

emp_1.fullname = 'Calvin Coolidge'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# property decorators allow us to define a method, but we can use it like an attribute
del emp_1.fullname
