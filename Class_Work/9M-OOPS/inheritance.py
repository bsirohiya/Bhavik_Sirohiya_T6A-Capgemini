# class Parent:

#     @staticmethod
#     def greet():
#         print("hehehehe")

# class Child(Parent):

#     @staticmethod
#     def greet():
#         print("hahaha")

# c1 = Child()
# c1.greet()

class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary) 
        self.department = department

e1 = Manager("bxs", 11, "sk")
print(e1.department)
print(e1.name)
print(e1.salary)