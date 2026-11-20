# Create a function to calculate the sum of all elements in a list.

def list_sum(numbers):
    total = 0

    for i in numbers:
        total = total + i

    return total


my_list = [10, 20, 30, 40, 50]

result = list_sum(my_list)

print("Sum:", result)