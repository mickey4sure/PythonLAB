#7.WAP to compute distance between two points (x1, y1) and (x2, y2) entered by user.

import math
x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))
#Calculating distance using distance formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between points ({}, {}) and ({}, {}) is: {}".format(x1, y1, x2, y2, distance))

