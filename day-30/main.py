# # FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# ZeroDivisionError
print(5/0)

# try, except, else, finally
# FileNotFoundError
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
#
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file.close()
#     print("File was closed")

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
#
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     raise TypeError("this is an error that I made up.")

# height = float(input("Height: "))
# weight = int(input("weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)




