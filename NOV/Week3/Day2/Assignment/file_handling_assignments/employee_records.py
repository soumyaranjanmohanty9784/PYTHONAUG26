# Question 2: Employee Records

with open("employee_records.txt", "w") as file:

    for i in range(5):
        print("\nEnter Employee", i + 1, "Details")

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = input("Enter Monthly Salary: ")

        file.write("Employee ID: " + emp_id + "\n")
        file.write("Name: " + name + "\n")
        file.write("Department: " + department + "\n")
        file.write("Salary: " + salary + "\n")
        file.write("----------------------\n")


with open("employee_records.txt", "r") as file:
    print("\nEmployee Records")
    print(file.read())