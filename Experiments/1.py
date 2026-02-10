#WAP a program to write hello world! in four different ways

print("Hello World!")

print(input())

a= "Hello" 
b= "World"
print("I am saying {} to the {}".format(a,b))

def hiworld():
    return "Hello World"
print(hiworld())                                                                                                 

import sys
sys.stdout.write("Hello World!")