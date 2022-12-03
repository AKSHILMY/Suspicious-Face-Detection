class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+" "+last+"@gmail.com"
        self.pay = pay

    def fullname(self):
        return '{}-{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay*self.raise_amt
        return self.pay


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first=first, last=last, pay=pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init(self, first, last, pay, employees=None):
        super().__init__(first=first, last=last, pay=pay)


dev_1 = Developer("Akeel", "Ahmed", 30000, "Python")
dev_1.apply_raise()
print(dev_1.pay)
