# Question 1: College Information

college_name = input("Enter College Name: ")
location = input("Enter Location: ")
year = input("Enter Establishment Year: ")
departments = input("Enter Number of Departments: ")


with open("college_info.txt", "w") as file:
    file.write("College Name: " + college_name + "\n")
    file.write("Location: " + location + "\n")
    file.write("Establishment Year: " + year + "\n")
    file.write("Number of Departments: " + departments + "\n")


with open("college_info.txt", "r") as file:
    data = file.read()

print("\nCollege Information")
print(data)