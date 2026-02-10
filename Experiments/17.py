#17. WAP to access the range of the characters of the string or accessing the substring of a string.
statement ='Hello World'
print (statement[0:5])  #OUTPUT:Hello
print (statement[6:11]) #OUTPUT: World
print (statement[:5])   #OUTPUT: Hello (start index is optional, defaullt to 0)
print (statement[6:])   #OUTPUT: World (end index is optional, defaullt to end index)
print (statement[-5:0]) #OUTPUT: World