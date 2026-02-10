Features of Python

Python provides many useful features and these features make python widely popular.

We have listed a number of essential features included in python:

1\. easy of use and learn

2\. object oriented language

3\. GUI programming support

4\. dynamic memory allocation

5\. libraries and frameworks



Program

01\. WAP to print hello world in  four different ways.







Where is Python Used???

Python is a general purpose popular programming language used in almost every technical field use in various python

Data Science

Artificial Intelligence

Machine learning

Data Communication

Web Development



Python has wide range of libraries and frameworks widely used in various field such as machine learning

such as artificial intelligence, web applications. We define some popular frameworks and libraries of











KIBI: it is a framework for building application

Pygames: It is a library used for game development field





Applications of Python

Python contributes in it's Importance in varieties of applications because of it's various features which makes

python highly readable easy to use and maintain manageable and reusable.

Python plays a crucial role in the field of gaming, web development and data analytics and plays a major role in

the field of AI.

Python has been the preferred language for developers in the following areas:

Web Development

Data science

CAD

Artificial Intelligence and Machine Learning

Game Development

Networking And Security

Data Analytics

Robotics





Every non zero number is true and every zero value number is false...



The IDLE integrated Python development environment is both written in Python

with tkinter and shipped and installed with the Python package (if you have a recent

Python interpreter, you should have IDLE too; on Windows, click the Start button,

select the Programs menu, and click the Python entry to find it). IDLE provides

syntax-coloring text editors for Python code, point-and-click debugging, and more,

and is an example of tkinter’s utility.











Keywords in python: 35



Python Literals

These are fixed constant values assigned to variables or used directly in expressions.

 The constant values are of types such as numbers, strings, Booleans, collection, or other special identifiers unlike

 the variables above literals are immutable which means they cannot be changed after being defined

                       Types of Literals









Variable naming convention



A variable name can contain only letters ,numbers or underscore.

for example

           abc\_n = 10

           abc@#! = 10 \[wrong]



A variable name can start with a letter or an underscore but not with a number.



Spaces are not allowed in a variable names.

Variable names should be short and descriptive.

Variable names are case sensitive.



For multiword variable names any of the following **conventions** can be followed

a. Camel case- words are capitalized

b. Pascal Case- same as camel case but first word is also capitalized

c. Snake Case- Words are separated by underscore



###### Chained Assignment Variable

Python allows chained assignment which help in assigning some values to multiple variables which helps assigning some

values to multiple values in the same line.



implicit

python will forcefully do the work

explicit

user will forcefully make python do the work



Python is a dynamic typed language allowing us not to define the datatypes of the variables explicitly however, python offers us the accessibility to convert one datatype into another

##### Type Conversion

It is the process in programming to convert one type of number into another python primarily offers two ways to convert the type of the variable.

###### Implicit Type Conversion(automatically)

Python converts smaller datatypes to larger ones automatically.

for example

 

###### Explicit Type Conversion(Manually)

Programmers use python's built functions like int(), float(), complex() and more to manually convert one datatype into another



 











In Python, operators are the symbols used to perform a specific operation on different values and variables(expressions).

Operation on different values and variables. These values and variables are considered as the operands on which the operators are applied.



###### TYPES OF PYTHON OPERATORS

**ARTHEMATIC OPERATORS
COMPARISON OPERATORS
ASSIGNMENT OPERATORS:** Using the right operator for assigning the right expression values
**LOGICAL OPERATORS
BITWISE OPERATORS
MEMBERSHIP OPERATORS** We can verify the membership of a value in python data structure using the python membership operators. The result is said to be true if the value found inside the data structure like list, tuples or dictionary otherwise, it returns false.



In :- If the first operand is present in second operand(sequence), it is evaluated to be true, if sequence can either be a list, tuple or a dictionary.

NOT IN :- If the first operand(value and variable) is not present in the second operand(sequence) it is evaluated to be true sequence can either be a list, tuple or dictionary.



**IDENTITY OPERATORS** Python offers two identity operators that are used to check if two values are located in the same part of memory:

a. Is: If the references on the both side point to the same object then, it is determined to be true.

b. Is Not: If the references on both side do not point at the same object then, it is determined to true.







##### STRING

A string in python is a sequence of characters enclosed.

for example: "Hello world" is a string consisting of a sequence of characters such as 'Hello World' anything including letters, numbers,

symbols and even wide spaces withing the quotation marks is treated as a string in python.

Python doesn't have a character data type, therefore a single character is considered as a string of length 1.



###### CHARACTERSTICS OF STRING:



1\. IMMUTABLE: Cannot be changed.

2\. ORDERED: Characters have fixed positions.

3\. ITERATABLE: Can loop through characters.

4\. SUPPORTS SLICING: Can extract substrings.

5\. HOLDS ANY CHARACTERS: Letters, numbers, symbols, spaces.

6\. UNICODE SUPPORT: Handles all languages and emojis.

7\. DYNAMIC LENGTH: Any size from zero to huge.



1\. IMMUTABLE: Once a string is created, it cannot be changed. Any operation that modifies a string

&nbsp;  will create a new string instead of altering the original one.

2\. ORDERED: Strings are ordered collection of characters where each character has a fixed index(starting from zero)
   we can access the characters using there position.

3\. ITERATABLE: we can iterate each characters of a string  using python loops



###### 14. Experiment

Creating a String 
We can create a String using a single quotation marks('') or double quotation marks("")

Multiline string:
In case, we want a string to represent multiple lines then, we can make use of triple quotations(''' ''')or(""" """)
to create a multiline string.

Accessing characters in a String
In Python, Strings are sequences of characters that can be exceed individually with the help of indexing
Strings are indexed 0 from the start and -1 from the end.
This indexing helps us retrieve particular characters from the string.

Accessing string with negative indexing:
In python, we are allowed to use negative addresses references in order to access the characters from the back of the string.
For example: -1 refers to the last character, -2 refers to second last character and so on

## 17. Experiment
##### String Slicing
Slicing is a way in python that allow us to extract a portion of a string by specifing the start and end indexes. The format for 
slicing the string is 
"String_name[start:end]"
where the start is the index where the slicing began and end is the index where it ends 

##### String Immutability
String in python is an immutable datatype that can not be changed after it's creation however we can manipulate strings using 
various methods like Slicing, Concatination or Formatting in order to create new strings on the basis of the original one.

#19. WAP to delete a string
msg = "Python"
del msg
print (msg)

##### UPDATING A STRING:
String is an immutable datatype which cannot be modified however we can update a part of a string by creating a new string itself.

#20.WAP to updating a string in python
given_str = "Welcome learners!"
print("given String", given_str)

new_str1 ="W" + given_str[1:]
new_str2 = given_str.replace("learners", "to Students")
print("New String 1: ", new_str1)
print("New String 2: ", new_str2)

### Common String Method
Python offers many built in methods for string manipulations. These methods allow us to determine the lenght of a string,
change it's cases, validate it, split and join, search and find substring and many other.

i. len() function: It is used to determine the lenght od the string. This function returns the total no. of characters in a given
string.

ii. upper() and lower(): In Python, the upper() method is used to convert all the characters of the string to uppercase whereas, 
   the lower method allows us to convert all the characters of the string to lowercase.

#22. WAP to display the upper() and lower() method use in python

iii. Strip and Replace method: Strip allows us to remove thr leading and trailing wide spaces from the string whereas, Replace is 
used to replace all the ouccurences of a particular substring with another.

#WAP to demonstrate the removing of spaces and replace subtring using string in pyhton.




































 

 

