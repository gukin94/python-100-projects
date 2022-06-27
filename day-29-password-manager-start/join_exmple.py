myList = ["John", "Peter", "Vicky"]

# method 1
new_list = str()
for item in myList:
    new_list += item
print(new_list)

# method 2
# x = "".join(myList)
# print(x)