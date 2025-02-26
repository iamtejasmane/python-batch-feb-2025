# Arithmetic Operators

# Basic arithmetic operations
# +  Addition
# -  Subtraction
# *  Multiplication
# /  Division
# // Floor Division (Quotient without remainder)
# %  Modulus (Remainder of division)
# ** Exponentiation (Power calculation)

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("Floor division:", a // b)  # 10 / 3 = 3.333 => 3 (integer result)
print("Modulus:", a % b)  # Remainder of division
print("Exponentiation:", a ** b)  # 10^3 = 1000

# Comparison Operators - Returns True or False

# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to

c = 10
d = 10

print("Not equal:", c != d)  # False because 10 == 10
print("Less than:", c < d)   # False because 10 is not less than 10
print("Less than or equal to:", c <= d)  # True because 10 is equal to 10

# Logical Operators - Returns True or False

# and - Returns True if both conditions are true
# or  - Returns True if at least one condition is true
# not - Reverses the result

x = 5
y = 10

print("Logical AND:", x > 2 and y > 5)  # True (Both conditions are true)
print("Logical OR:", x > 2 or y < 5)  # True (At least one condition is true)
print("Logical NOT:", not (2 > 10))  # True (Reverses False to True)

# Membership Operators - Checks if a value is in a sequence

# in     - Returns True if a value is present in the sequence
# not in - Returns True if a value is NOT present in the sequence

fruits = ['apple', 'banana', 'cherry']  # Corrected spelling from 'bannana'
numbers = [10, 20, 40, 50, 60]

print("Fruits list:", fruits)
print("Is 20 not in numbers?", 20 not in numbers)  # False because 20 is in numbers
print("Is 'mango' not in fruits?", 'mango' not in fruits)  # True because 'mango' is not in fruits
