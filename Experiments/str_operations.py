# Program to demonstrate String Operations

str1 = "Hello"
str2 = "World"

# 1. Length of String
length = len(str1)
print(f"Length of '{str1}': {length}")

# 2. Concatenation (Joining)
joined_str = str1 + " " + str2
print(f"Concatenation: {joined_str}")

# 3. Repetition
repeated_str = str1 * 3
print(f"Repetition: {repeated_str}")

# 4. Slicing
# Syntax: string[start:stop]
text = "PythonProgramming"
sliced_text = text[0:6]  # Extracts characters from index 0 to 5
print(f"Slicing '{text}' [0:6]: {sliced_text}")

# 5. Comparison
# Checks if str1 is equal to str2
are_equal = (str1 == str2)
# Checks if str1 is not equal to str2
not_equal = (str1 != str2)

print(f"Comparison ({str1} == {str2}): {are_equal}")
print(f"Comparison ({str1} != {str2}): {not_equal}")