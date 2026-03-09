# # Class is the blueprint of object(Instance)
# class Student:
#     collegeName = "JECRC University"  # collegeName -> Stored in Key layer, "JECRC University"-> Its address(0X12) is stored in Value layer (Whole in value space) and Key layer address will be stored in variable space and its name is going to be the name of class i.e Student here.
#     location = "Jaipur"

# # Object creation-
# st1 = Student()

# # print(Student)
# # print(st1)

# st1.name = "Ram"
# print(st1.name)

# s2 = Student()
# print(s2.name)


#-----------------------------------------------------------------------------------------------------------------

class Employee:
    company = "Capgemini"
    location = "Mumbai"
    childCompany = "Sogeti"

e1 = Employee()
e1.name = "Ram"
e1.id = "ram@001"
e1.salary = 1000000

e2 = Employee()
e2.name = "Hanuman"
e2.id = "hanu@002"
e2.salary = 100000

print(e1.name)
print(e1.id)
print(e1.salary)
print(e1.company)
print(e1.location)
print(e1.childCompany)

# It is hard to do this manually(lengthy), what if we have to store 1000 enteries.
# So to reduce this hard work we use constructor