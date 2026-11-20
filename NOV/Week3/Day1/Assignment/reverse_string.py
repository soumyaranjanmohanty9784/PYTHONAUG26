# Create a function to reverse a string.

def reverse_string(text):
    return text[::-1]


name = input("Enter a string: ")

result = reverse_string(name)

print("Reverse:", result)