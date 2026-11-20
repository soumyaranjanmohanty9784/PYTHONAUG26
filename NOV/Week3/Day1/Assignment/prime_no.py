# Create a function to check whether a number is prime.

def check_prime(num):
    if num <= 1:
        print("Not a Prime Number")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            return

    print("Prime Number")


number = int(input("Enter a number: "))

check_prime(number)