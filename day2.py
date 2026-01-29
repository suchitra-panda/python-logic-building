
# Python Logic Building – Day 2
# Conditional Statements Practice

# Problem 1: Largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("a is bigger")
elif b > a:
    print("b is bigger")
else:
    print("Both are equal")

print("----------------------------")

# Problem 2: Even, Odd or Zero
num = int(input("Enter a number: "))

if num == 0:
    print("Zero")
elif num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("----------------------------")

# Problem 3: Pass or Fail
marks = int(input("Enter marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")

print("----------------------------")

# Problem 4: Divisible by 3 and 5
a = int(input("Enter a number: "))

if a % 3 == 0 and a % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print(a, "is not divisible by 3 and 5")

print("----------------------------")

# Problem 5: Largest of three numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x > y and x > z:
    print("Largest number is", x)
elif y > x and y > z:
    print("Largest number is", y)
else:
    print("Largest number is", z)

print("----------------------------")

# Problem 6: Leap Year Check
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")

print("----------------------------")

# Problem 7: Grade System
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

print("----------------------------")

# Problem 8: Vowel or Consonant
char = input("Enter a single character: ").lower()

if char in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

print("----------------------------")

# Problem 9: Simple Login System (Nested if)
username = input("Enter username: ")
password = int(input("Enter password: "))

if username == "admin":
    if password == 1234:
        print("Login successful")
    else:
        print("Login failed")
else:
    print("Login failed")

print("----------------------------")

# Problem 10: Eligibility to vote (Logical operator)
age = int(input("Enter age: "))
country = input("Enter country: ").lower()

if age >= 18 and country == "india":
    print("Eligible to vote")
else:
    print("Not eligible")
