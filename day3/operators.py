
# Arithmetic Operators

# + addition
# - subtraction
# * multiplication
# / division
# // floor division
# % Modulus
# ** Exponentiation

a = 10
b = 3

print("Addition", a + b)
print("Subtraction", a - b)
print("Mulitplication", a * b)
print("Division", a / b)

print("Floort divsion:", a // b) # 3.333 => 3
print("Modulus", a % b)
print("Exponentiation:", a ** b)

# Comparisoin Operators = True or False

# == - quals to 
# != - not equal to 
# > greater than
# < less than 
# >= Greater than or quals to 
# <= Less than or equal to


c = 10
d = 10


print(c != d)

print(c < d)
print(c <= d) # Less than && equal


# Logical Operators. => True || False

# and ==> &&
# or ==> ||
# not ==> !

x = 5
y = 10

print( x > 2 and y > 5) # Returns True if both conditions are true otherwise it returns false

print( x > 2 or y < 5) # Return True if at least one condition is true

print( not 2 > 10) # Reverse the result


# Membership operators - True
# in -  Returns True if a value is in the sequest
# not in - Reverse the in result.

fruits = ['apple', 'bannana', 'cherry']

numbers = [10, 20, 40, 50, 60]

print(fruits)

print(20 not in numbers)
print('mango'  not in fruits)




