#Write a program to write hello world! in four different ways
#WAP to determine basic datatypes in python
#WAP to print dynamic typing objects.
#WAP to print  "Hello, username" with a user's name on Python.
#WAP to add two numbers entered by user on python
#WAP to find the average of two numbers entered on python.
#WAP to compute distance between two points taking input from the user.
import math
x1 = float(input("Enter x coordinate of first point: "))
x2 = float(input("Enter x coordinate of second point: "))
y1 = float(input("Enter y coordinate of first point: "))
y2 = float(input("Enter y coordinate of second point: "))
distance = math.sqrt((x2 - x1)**2 +(y2 - y1)**2)
print("\nDistance between two points is: ",distance)

#WAP to add .py that takes two numbers as commandline argument and print their sum.
'''
import sys
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
sum = num1 + num2
print("Sum =", sum)'''

#write a program to use variable naming conventions and print all the variables.
#WAP to use chained assignment variable and print the result.
