# 8/03/20 - for loop
# colors = [11, 34, 98, 43, 45, 54, 54]

# for color in  colors:
#     print(color)

# more prctice print colors if greater than 50!

# colors = [11, 34, 98, 43, 45, 54, 54]

# for color in colors :
#     if color  > 50:
#         print(color)


# loop int and big colors

# colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

# for color in colors:
#     if isinstance(color, int) and color > 50:
#         print(color)

# looping colors but just getting the integer

# colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

# for color in colors:
#     if isinstance(color, int):
#         print(color)


# traversing a dictionary with a loop

# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

# for key, value in phone_numbers.items():
#     print("%s: %s" % (key, value))

# replacing a variable with a new string

# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

# for value in phone_numbers.values():
#     print(value.replace("+", "00"))

# ex of a while loop

# while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
# print("It's not yet 19:30:20 of 2090.8.20")

# appending number to make a new array

# temos = [223, 345, 621, 356 ]

# new_temos = []

# for temo in temos:
#     new_temos.append(temo /10)

# print(new_temos)

# # alt
# new_temos = [temo / 10 for temo in temos]

# print(new_temos)

# temos = [223, 345, 621, 356 ]

# new_temos = []

# new_temos = [temo / 10 for temo in temos if temo != 356]

# checking for results with conditionals

# lst = [64, 39, -39, -204]
# def perri(lst):
#     return [i for  i in lst if not isinstance(i, str)]

# def pery(lst):
# return [i for i in lst if i > 0

# changing data in str from no data to 0

# def zeros(lst):
#     return [i if not isinstance(i, str) else 0 for i in lst]

# float to sum

# def mathhh(lst):
#     return sum([float(i) for i in lst])

# function with a multi params

# def foo(s1, s2):
#     return s1 + s2

# getting the sum and the length

# def m(*args):
#     return sum(args) / len(args)

# soting method

# def mac(*args):
#     args = [x.upper() for x in args]
#     return sorted(args)


# keyword args for arbitray stuff
# # def find_sum(**kwargs):
#     return sum(kwargs.values())

# print(find_sum(x=4, y=3, z=2))

# how to open a file with python
# file = open("bear.txt")
# content = file.read()
# print(content)

# openin to get a set number of characters
# myfile = open("bear.txt")
# content = myfile.read()
# print(content[:90])

# using function to file process

# def ct(character, filepath="bear.txt"):
#     file = open(filepath)
#     content = file.read()
#     return(content.count(character))

# with and making a new
# with open("file.txt", "w") as file:
#     file.write("snail")
