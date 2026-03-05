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

a = 9
def kez():
    global a
    a = 19
    print(a)
    print(id(a))
    return a

#main
print(id(a))
print(a)
print(kez())
print(a)#the global value will not change in the main scope


