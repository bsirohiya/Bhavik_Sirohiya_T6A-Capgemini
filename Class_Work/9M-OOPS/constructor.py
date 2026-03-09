class Employee:
    company = "Capgemini"
    location = "Mumbai"
    childCompany = "Sogeti"

    # Constructor -> Automatically called when object is created
    #   1. A constructor defines what happens when your object will be created.
    def __init__(self, name, id, salary, department, age):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department
        self.age = age

    def display(self):
        print(f"Name - {self.name}")
        print(f"id - {self.id}")
        print(f"Salary - {self.salary}")
        print(f"Department - {self.department}")
        print(f"Age - {self.age}")

e1 = Employee("Ram", "ram@001", 1000000, "Creator", 10)
# print(e1.name, e1.id, e1.salary)
e1.display()