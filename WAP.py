#WAP a program to write hello world! in four different ways
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

#WAP to use variable naming conventions and print all the variables.
#WAP to use chained assignment variable and print the result.
#WAP to demonstrate all the python operators like arithmetic, comparison, assignment, bitwise, logical, identity and membership operators.
#WAP to perform type conversion or casting in python programming like implicit conversion and explicit conversion.
#WAP to create a string in python
'''
CREATING a STRING
name ="Jaspreet"
name ='Jaspreet' ''' 
#name ='''Jaspreet'''
'''
print(name)
print(name)
print(name)
'''
#14. WAP to create Multi-line String in Python.
str = ''' Jasper 
          Jean 
          Farnandez'''
print("Multiline String: ",str)

#15. WAP to access individual characters in a String.
statement = 'HELLO'
print (statement[0])
print (statement[2])

#16. WAP to access individual characters from the last in a String.
statement = 'HELLO'
print (statement[-1])
print (statement[-4])

#17. WAP to access the range of the characters of the string or accessing the substring of a string.
statement ='Hello World'
print (statement[0:5])  #OUTPUT:Hello
print (statement[6:11]) #OUTPUT: World
print (statement[:5])   #OUTPUT: Hello (start index is optional, defaullt to 0)
print (statement[6:])   #OUTPUT: World (end index is optional, defaullt to end index)
print (statement[-5:0]) #OUTPUT: World


### STRING IMMUTABILITY

#18. WAP to demonstrate string immutability in Python
msg = "hellostudents"
print("Given String: ", msg)
msg ='H'+msg[1:5] +'S'+msg[6:]
print("New msg: ",msg)
print(msg[0:5])


#19. WAP to delete a string
msg = "Python"
del msg
print (msg)


#20.WAP to updating a string in python
given_str = "Welcome Learners!"
print("given String", given_str)

new_str1 ="W" + given_str[1:]
new_str2 = given_str.replace("Learners", "Students")
print("New String 1: ", new_str1)
print("New String 2: ", new_str2)


#21. WAP to determine the lenght of a string in python using len()
msg = "Python is high level language"
print("String: ",msg ,"\nLenght of the given string: ",len(msg))

#22. WAP to display the upper() and lower() method use in python
msg = "PythonProgramming"
print("Given String: ", msg)            
print("Upper Case: ", msg.upper())
print("Lower Case: ", msg.lower()) 

#23. WAP to demonstrate the removing of spaces and replace subtring using string in pyhton.
msg = "     Python Programming      "
print("String 1: ", msg)
print("After removing spaces from the both sides: ")
print(msg.strip())