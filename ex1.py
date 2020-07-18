import datetime
mynow = datetime.datetime.now()
print(mynow)

mynum = 7
mytext = "hippy"

print(mynum, mytext)

str = "8"
float = 10.2
x = 8

# # make a list with  a float a int a str
# temperatures = [1, 29.7, "34"]

# # make a list that has a integer float and a str in list
# rainfall = [1, 29.7, "34",  [23, 34, 12]]

# max method
# student_grades = [9.1, 8.8, 7.5]
# max_value = max(student_grades)
# print(max_value)


# student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
# print(student_grades.count(10.0))

# username = "Python3"
# print(username.lower())

# Examples of a dictionary
# # day_temperatures = {
#     "morning" : 10.06,
#     "noon" : 20.4,
#     "evening" : 13.7
# }

# variable with tuple inside
# color_codes = ((1, 2,3), (5,6,7), (123,135,158))
# 

# complex dict with tuples 

# day_temperatures = {'morning' : (7.9, 9.0, 12.5), "noon" : (34.5, 67.9, 3.9), 'evening' : (12.8, 27.12, 35.8) 
    # }

# appending info to another list
# seconds = [1.2323442655, 1.4534345567, 1.023458894]
# current = 1.10001399445
# seconds.append(current)

# serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
# print(serials[2])

# serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
# print(serials[0], serials[2], serials[5])
# 

# workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# weekend = ["Sat", "Sun"]
# workdays.append(weekend[0])

# remove method 

# seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
# seconds.remove(1.4534345567)

# seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
# seconds.remove(1.4534345567) 
# seconds.remove (1.023458894)
# seconds.remove(1.10001399445)

# slicing

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[1:4])

# length function

# def lengther(lst):
#     return len(lst)

# area of a square
# def foo(a):
#     return a * a

# oz to militers

# def sick(oz):
#     return oz * 29.57353


# print or return

# one is used for simple things like printing values and the other is for executing a function 

# review of conditionals if, else, and, or. 7/11/2020


# practice conditionals
# def foo(password):
#     if len(password) >= 8:
#         return True
#     else:
#         return False

# def foo(temperature):
#     if temperature > 7:
#         return "Warm"
#     else:
#         return "Cold"

# # def temp(temperature):
#     if temperature > 25:
#         return "Hot"
#     elif 25 >= temperature >= 15:
#         return "Warm"
#     else:
#         return "Cold"


# summary of everything reviewed -7/17/20

# Define a function:

# def cube_volume(a):
#     return a * a * a
# Write a conditional block:

# message = "hello there"
 
# if "hello" in message:
#     print("hi")
# else:
#     print("I don't understand")
# Write a conditional block of multiple conditions:

# message = "hello there"
 
# if "hello" in message:
#     print("hi")
# elif "hi" in message:
#     print("hi")
# elif "hey" in message:
#     print("hi")
# else:
#     print("I don't understand")
# Use the and operator to check if both conditions are True at the same time:

# x = 1
# y = 1
 
# if x == 1 and y==1:
#     print("Yes")
# else:
#     print("No")
# Output is Yes since both x and y are 1.

# Use the or operator to check if at least one condition is True:

# x = 1
# y = 2
 
# if x == 1 or y==2:
#     print("Yes")
# else:
#     print("No")
# Output is Yes since x is 1.

# Check if a value is of a certain type with:

# isinstance("abc", str)
# isinstance([1, 2, 3], list)
# or

# type("abc") == str
# type([1, 2, 3]) == lst