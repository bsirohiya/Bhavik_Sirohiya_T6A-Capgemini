#Main and important inbuild functions of DSs-

# String - upper, lower, swapcase, replace, capitalize, title, split, join, index, count, isupper, islower, isdigit, rstrip, lstrip, strip.

# List - append, insert, pop, remove, sort, reverse, count, index.

# Set - add, pop, remove, union, intersection, difference, clear, update.

# Dict- keys, values, items, get, pop, popitems, update, clear.
    
#type of UD-Functions

# with arguments and with return type
# def addIt(a, b):
#     return a+b

# #main
# print(addIt(5,6))

# with arguments and without return type
# def addIt(a, b):
#     print(a+b)

# #main
# addIt(5,6)

# # without arguments and with return type
# def addIt():
#     return 5+6

# #main
# print(addIt())

# without argument and without return value
# def addIt():
#     print(5+6)

# addIt()


# Task 1
# li = eval(input("Enter list no"))
# resLi=[]
# def findNeg():
#     for i in li:
#         if i < 0:
#             resLi.append(i)
#     return resLi     
   
# print(findNeg())

# a = 9
# def kez():
#     global a # Here by declaring it as global, now it has power to change the value of a
#     a = 19
#     print(a)
#     print(id(a))
#     return a

# #main
# print(id(a))
# print(a)
# print(kez())
# print(a)#the global value will not change in the main scope


# a = 100

# def fun1():
#     a = 10
#     b = 5
#     print (a+b)

#     def fun2():
#         b = 500 # this fun can access but can't change it
#         print(b)
#     fun2()   
#     print(b) 
# fun1()


# But if we want to change it we should declare it as nonlocal
# a = 1
# def fun1():
#     a = 10
#     b = 5
#     print (a+b)

#     def fun2():
#         nonlocal b
#         b = 500 # this fun can access but can't change it
#         print(b)
#     fun2()   
#     print(b) 
# fun1()


# Task1
# def prodList(li):
#     prod = 1
#     for i in li:
#         prod *= i
#     return prod

# print(prodList(eval(input("Enter a list"))))    

# Task2 - Print initial index of char present in a given string

def findFirstIndex(string, char):
    for i in range(0, len(string)):
        if string[i] == char:
            return i
    return "No such character"

print(findFirstIndex(input("Enter a string: "), input("Enter the char to find: ")))