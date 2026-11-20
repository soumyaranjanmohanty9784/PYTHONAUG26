# Create a function to check whether a number is even or odd.

def check_even_odd(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


number = int(input("Enter a number: "))

check_even_odd(number)