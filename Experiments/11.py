'''11.WAP to demonstrate all the python operators like arithmetic, comparison, assignment, 
bitwise, logical, identity and membership operators.
Arithmetic Operators'''
a = 10
b = 5
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
# Comparison Operators
print("\nComparison Operators:")
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)
# Assignment Operators
print("\nAssignment Operators:")
c = a
print("Value of c after assignment:", c)
c += b
print("Value of c after addition assignment:", c)
c -= b
print("Value of c after subtraction assignment:", c)
c *= b
print("Value of c after multiplication assignment:", c)
c /= b
print("Value of c after division assignment:", c)
c //= b
print("Value of c after floor division assignment:", c)
c %= b
print("Value of c after modulus assignment:", c)
c **= b
print("Value of c after exponentiation assignment:", c)
# Bitwise Operators
print("\nBitwise Operators:")
x = 6  # 110 in binary
y = 3  # 011 in binary
print("Bitwise AND:", x & y)
print("Bitwise OR:", x | y)
print("Bitwise XOR:", x ^ y)
print("Bitwise NOT:", ~x)
print("Left Shift:", x << 1)
print("Right Shift:", x >> 1)
# Logical Operators
print("\nLogical Operators:")
p = True
q = False
print("Logical AND:", p and q)
print("Logical OR:", p or q)
print("Logical NOT:", not p)
# Identity Operators
print("\nIdentity Operators:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list2:", list1 is not list2)
print("list1 is not list3:", list1 is not list3)
# Membership Operators
print("\nMembership Operators:")
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)
print("6 in my_list:", 6 in my_list)
print("3 not in my_list:", 3 not in my_list)
print("6 not in my_list:", 6 not in my_list)

