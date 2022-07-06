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

# try:
#     print("asd")
# except ZeroDivisionError
# print(5/0)

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
# #
# # except KeyError as error_message:
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
#     print(a_dictionary["font_color"])
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

height = float(input("Height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

# try:
#     # 에러가 발생할 수 있는 코드를 이곳에 넣습니다.
#
# except :
#     # 만약 에러가 발생한다면 이 구문이 실행됩니다.
#
# else:
#     # 만약 에러가 발생하지 않는다면 이 구문이 실행됩니다.
#
# finally:
#     # 에러 발생 여부와 관계없이 이 구문은 무조건 실행됩니다.



# try:
#     print(5/0)
# except ZeroDivisionError as e:
#     print(e)