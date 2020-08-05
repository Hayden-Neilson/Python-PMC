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