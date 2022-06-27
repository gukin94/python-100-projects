# myList = ["John", "Peter", "Vicky"]
#
# # method 1
# new_list = str()
# for item in myList:
#     new_list += item
# print(new_list)


myDict = {"name": "Gukin", "country": "Korea"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)