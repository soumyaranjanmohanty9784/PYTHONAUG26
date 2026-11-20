# Question 8: Examination Result

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

total = 0
failed = False

for i in range(5):

    marks = int(input("Enter Subject " + str(i + 1) + " Marks: "))

    total += marks

    if marks < 33:
        failed = True

percentage = total / 5

if failed:
    result = "Fail"
else:
    result = "Pass"

# Write result
with open("exam_result.txt", "w") as file:

    file.write("Student Name: " + name + "\n")
    file.write("Roll Number: " + roll + "\n")
    file.write("Total Marks: " + str(total) + "/500\n")
    file.write("Percentage: " + str(percentage) + "%\n")
    file.write("Result: " + result + "\n")

# Read result
with open("exam_result.txt", "r") as file:
    print("\nExamination Result")
    print(file.read())