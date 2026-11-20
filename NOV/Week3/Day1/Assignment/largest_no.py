# Create a function to find the largest of three numbers.

def largest(a, b, c):
    if a > b and a > c:
        print("Largest:", a)
    elif b > a and b > c:
        print("Largest:", b)
    else:
        print("Largest:", c)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest(num1, num2, num3)