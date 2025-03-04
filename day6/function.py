# Functions

def greet():
    print("Hello! Welcome to Python functions.")

greet()  # Calling the function
greet()

print("I am on line 5.")

# Syntax 
# def function_name():
#     Function body...
#     Code...

def say_hello():
    print("Hello, students!")

say_hello()

# Function with parameters
# Parameters (input variables)

def greet(name):
    print(f"Hello, {name}")

greet("Tejas")
greet("Stefno")

a = 10
b = 20

print("Sum", a + b)

def add(a, b):
    print("Sum :", a + b)

add(10, 20)
add(30, 50)
add(-5, -10)
add(50, -5)

# Default parameters 

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Tejas")  # Uses given value
greet()  # Uses the default value

def student_details(name, age):
    print(f"Name: {name}, Age: {age}")

student_details("Tejas", 30)  # Order of the parameters matters
student_details(age=30, name="Tejas")  # Order doesn't matter

# Arbitrary arguments (*args and **kwargs)

def sum_numbers(*numbers):
    print(numbers)
    total = sum(numbers)
    print("Sum :", total)

sum_numbers(1, 2, 3, 4, 5, 7, 30, 50)  # Pass multiple values

counter = 0  # Global variable

def update_counter():
    global counter
    counter = counter + 1
    print("Counter", counter)

update_counter()
update_counter()
update_counter()
update_counter()
