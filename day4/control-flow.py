# Conditional Statements

# 1. if Statement
# Checks a condition and executes the indented block if the condition is True

# Example: Checking voting eligibility
# age = 15

# if age >= 18:
#     print("You are eligible to vote")

# 2. if-else Statement
# Executes one block if the condition is True, otherwise executes the else block

# age = 12

# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote yet.")

# 3. if-elif-else Statement
# Allows multiple conditions to be checked sequentially

# marks = 54

# # Grading System:
# # 90 and above      : Grade A
# # 75 to 89         : Grade B
# # 50 to 74         : Grade C
# # Below 50         : Grade F

# if marks > 100 or marks < 0:
#     print("Hey, please add proper numbers!")
# elif marks >= 90:
#     print("Congratulations! Your Grade is A!")
# elif marks >= 75:
#     print("Wow! Your grade is B")
# elif marks >= 50:
#     print("Work hard, your grade is C")
# else:
#     print("Sorry! You have failed!!")

# Basic arithmetic operations
# print("Division:", 10 / 2)  # Division
# print("Remainder:", 10 % 2)  # Modulus (Remainder)

# # Checking if a number is even or odd
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# User authentication system
username = input("Enter your username: ")
password = input("Enter password: ")

if username == "admin" and password == "Test1234":
    print("Login Successful")
else:
    print("Invalid Username or Password!")