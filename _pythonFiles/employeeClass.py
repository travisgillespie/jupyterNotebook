class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_employees += 1

    def fullName(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Count the number of employees created
print(Employee.num_of_employees)
emp1 = Employee("Travis", "Gillespie", 100000)
emp2 = Employee("Test", "User", 80000)
# emp3 = Employee("Test3", "User3", 60000)
# emp4 = Employee("Test4", "User4", 40000)
# emp5 = Employee("Test5", "User5", 50000)

print(Employee.num_of_employees)

# Apply a raise to emp1
emp1.fullName()
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
