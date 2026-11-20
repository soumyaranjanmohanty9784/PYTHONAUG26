# Create a function using args to calculate the sum of multiple numbers.

def calculate_sum(*args):
    total = 0

    for i in args:
        total = total + i

    return total


result = calculate_sum(10, 20, 30, 40, 50)

print("Total Sum:", result)