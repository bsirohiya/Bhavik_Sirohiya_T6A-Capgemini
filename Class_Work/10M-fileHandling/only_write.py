file = open('only_write.txt', 'w+')

file.write("Heading\n")
file.writelines([
    "Firstt\n",
    "sec\n",
    "thir\n",
    "four\n",
])
file.seek(0) # To make py interpreter to point a specific index
print(file.read())
file.close()