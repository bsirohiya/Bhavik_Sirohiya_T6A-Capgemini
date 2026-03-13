file = open("only_write.txt", "r")

# print(file.read())

# print(file.readline())
# print(file.readline())
# print(file.readline())

print(file.readlines())
file.close()