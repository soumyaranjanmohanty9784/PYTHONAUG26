# Question 6: Copy Notes

with open("python_notes.txt", "w") as file:

    file.write("Python is a programming language.\n")
    file.write("Python is easy to learn.\n")
    file.write("Python supports OOP.\n")
    file.write("Python supports file handling.\n")

with open("python_notes.txt", "r") as file:
    data = file.read()

print("Original Notes:")
print(data)

with open("backup_notes.txt", "w") as file:
    file.write(data)

print("File Copied Successfully!")