import sys
sys.setrecursionlimit(4000)

# Factorial
# def fact(n):
#     factoriall = 1
#     while(n>0):
#         factoriall *= n
#         n -=1
#     print(factoriall)
# fact(1)


# Using RECURSION
def factt(n):
    if n==1 or n==0:
        return 1
    return n*factt(n-1)
print(factt(1600))