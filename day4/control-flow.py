# Coditional Statements 

# 1. if 

# Syntax: if <condtion>:


# eligibility for vote
age = 15

if age >= 18:
    print("You are eligilbe to vote")

# else 

# sytax:

# if condition:
#     Code...
# else: 
#     Code...

age = 25

if age >= 18:
    print("You are eligilbe to vote")
else:
    print("You are not eligible to vote yet.")

# elif

# sytax:

# if condition:
#     Code...
# elif condition2:
#     Code...
# else: 
#     Code...


marks = 95

# marks >= 90 : Grade A
# marks >= 75 : Grade B
# marks >= 50 : Grade C
# Below 50: Grade F

if marks > 100 or marks < 0:
    print("Hey please add proper numbers!")
elif marks >= 90:
    print("Congratulations! your Grade is A!")
elif marks >= 75:
    print("Wow! Your grade is B")
elif marks >= 50:
    print("Work hard, your grade is C")
else:
    print("Sorry! You are failed!!")


print("Division: ", 10 / 2)
print("Reminder: ", 10 % 2)

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

username = input("Enter your username: ")
password = input("Enter password: ")

if username == "admin" and password == "Test1234":
    print("Login Successful")
else:
    print("Invalid Username or Password!")