# Q1. Write a program to check whether a number is positive or negative.

# i = 10

# if i > 0:
#     print("Positive Number")
# else:
#     print("Negative Number")

# Q2. Write a program to check whether a number is even or odd.

# i = 15

# if i % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# Q3. Write a program to check voting eligibility.

# age = 18

# if age>=18:
#     print("Eligible for Voting")
# else:
#     print("Not Eligible for Voting")

# Q4. Write a program to find the largest of two numbers.

# a = 15
# b = 25

# if a > b:
#     print("A is Largest")
# else:
#     print("B is Largest")

# Q5. Write a program to calculate grades based on marks.


# mark = 90

# if mark >= 90:
#     print("Grade O")
# elif mark >= 80:
#     print("Grade A+")
# elif mark >= 70:
#     print("Grade A")
# elif mark >= 60:
#     print("Grade B")
# elif mark >= 50:
#     print("Grade C")
# elif mark >= 40:
#     print("Grade D")
# elif mark >= 30:
#     print("Grade E")
# else:
#     print("Fail")


# Q6. Write a program to check whether a number is positive, negative, or zero.

# num = -3

# if num > 0:
#     print("Poditive")
# elif num < 0:
#     print("Negetive")
# else:
#     print("Zero")


# Q7. Write a program to create a simple calculator using if-elif-else.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Addition =", a + b)
elif op == "-":
    print("Subtraction =", a - b)
elif op == "*":
    print("Multiplication =", a * b)
elif op == "/":
    print("Division =", a / b)
else:
    print("Invalid Operator")