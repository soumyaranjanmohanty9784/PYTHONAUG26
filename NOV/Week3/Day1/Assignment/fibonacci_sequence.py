# Create a recursive function to calculate the Fibonacci sequence.

def fibonacci(num):
    if num <= 1:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)


n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")