# Numeric Data Types

# 1. Integer - Whole numbers (positive, negative, or zero) without decimal points
age = 30
year = 2025
temperature = -5

# Checking the type of an integer variable
# print(type(temperature))

# 2. Float - Numbers with decimal points
height = 5.11
price = 99.99

# Checking the type of a float variable
# print(height, type(height))

# 3. Complex - Numbers with a real and imaginary part
num = 5j  # 'j' denotes the imaginary unit
print(num, type(num))

# Boolean - Represents True or False values
is_adult = True
is_child = False

# Checking the type of a boolean variable
# print(type(is_adult))

# Sequence Types

# 1. String - A sequence of characters enclosed in quotes
message = "Hello, World"

# Checking the type of a string variable
# print(type(message))

# 2. List - A mutable (modifiable) ordered collection
numbers = [10, 20, 30, 40, 50]  # List of integers
# print(numbers)
# print(type(numbers))

colors = ["red", "blue", "green", "orange"]  # List of strings
emp1 = ["John", "Week", 123200, 6.2, True]  # List with mixed data types
emp2 = ["John", "Week", 123200, 6.2, True]  # Another list with mixed data types

# Accessing elements of a list using index
# print(colors)
# print(colors[0])  # Accessing the first element

# Checking the type of a list
# print(type(colors))

# Modifying a list element (lists are mutable)
colors[1] = "yellow"  # Changing "blue" to "yellow"

# print(colors)

# 3. Tuple - An immutable (unchangeable) ordered collection
colors = ("red", "blue", "green")
print(colors)
print(colors[1])  # Accessing an element in the tuple

# The below statement is incorrect because tuples are immutable
# colors[1] = "yellow"

# Checking the type of a tuple
print(type(colors))

# Set - An unordered collection of unique elements

# Example list with duplicate values
duplicate_list = [10, 20, 30, 20, 60, 40, 50, 10, 80]
print(duplicate_list)  # List allows duplicates

# Creating a set to remove duplicates
numbers = {10, 20, 30, 20, 60, 40, 50, 10, 80}
print(numbers)  # Set stores only unique values
print(type(numbers))  # Checking the type of a set
