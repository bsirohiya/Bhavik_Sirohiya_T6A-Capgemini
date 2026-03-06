# Packing is of two types-
    # 1. Single packing (tuple packing)
    # 2. Double packing (dictionary packing)

# Single packing
# def findIndex(value, *tup):
#     for i in range(0, len(tup)):
#         if tup[i] == value:
#             print(tup)
#             return i
#     return -1    

# print(findIndex(10, 1,2,3,4,10,11,14))



# Double packing
# def doublePacFun(**dicti):
#     return dicti   

# print(doublePacFun(a="1", b=2, c=3))


# Unpacking
def unPacFun(a,b,d):
    print(a,b,d)

unPacFun(*"hel")    