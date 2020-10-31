#  Write a Python program to get the Python version you are using
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

#  Write a Python program to print the following string in a specific format (see the output):

print("Twinkle, twinkle, little star,\n How I wonder what you are! \n Up above the world so high, Like a diamond in the sky.\n Twinkle, twinkle, little star,\n How I wonder what you are")

# Write a Python program to display the current date and time.
import datetime
now = datetime.datetime.now()
print("current time and date:")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)
