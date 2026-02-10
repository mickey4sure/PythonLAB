#8.WAP to add .py that takes two numbers as command line argument and print their sum.

import sys
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
# "Calculating sum"
sum = num1 + num2 
# "Printing Result"
print("Sum =", sum)

#commandline 
'''Microsoft Windows [Version 10.0.26200.7623]
(c) Microsoft Corporation. All rights reserved.

D:\Python>python add.py 20 30
Sum = 50.0

D:\Python>''' 