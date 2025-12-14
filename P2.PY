class Employee:
    def __init__(self,name,salary):
       self.name = name
       self.salary = salary
    def annual_salary(self):
       return self.salary * 12
e1 = Employee("Amit",25000)
print("Annual Salary:",e1.annual_salary())