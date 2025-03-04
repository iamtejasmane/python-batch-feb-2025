# Loops

# Printing numbers manually
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)

# Using loops to reduce repetition

# 1. for loop
# Iterating over a list of fruits
fruits = ["apple", "banana", "cherry", "mango", "asldfk", "asdfasd"]

# for variable in sequence:
#     Code...

for fruit in fruits:
    print(fruit)
    
    if fruit == "apple":
        print("Cut it into half")
    
    if fruit == "mango":
        print("I want one more!")

print("Out of the loop")

# 2. Iterating over a string
word = "Tejas"

for letter in word:
    print(letter)

# 3. Find if a number is present in the list
nums = [10, 20, 30, 40, 50, 60]

n = int(input("Enter the number: "))

for num in nums:
    print(num)
    if num == n:
        print("Your number is present in the list:", num)
        break  # Exit loop once the number is found

# 4. Using range() function
# Generates a sequence of numbers

for i in range(10, 101, 10):  # Start at 10, go up to 100, step by 10
    print(i)

# 5. while loop
# Loop runs while the condition is True

# Counter variable
count = 1

while count <= 10:
    print("Count", count)
    count = count + 1  # Increment count

# 6. Infinite loop with user input (terminates when correct password is entered)
password = ""

while password != "Test123":
    password = input("Enter the password: ")
    if password != "Test123":
        print("Incorrect password, please try again")

print("Access granted")
