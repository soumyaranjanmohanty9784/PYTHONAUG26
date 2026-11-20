def add_employee():

    employee = {}

    employee["id"] = int(input("Enter Employee ID: "))
    employee["name"] = input("Enter Employee Name: ")
    employee["department"] = input("Enter Department: ")
    employee["salary"] = float(input("Enter Monthly Salary: "))

    print("\nEmployee Added Successfully!")

    return employee


def display_employee(employees):

    if len(employees) == 0:
        print("\nNo Employee Found!")
        return

    print("\n<<<<<<<<<<<<< EMPLOYEE DETAILS >>>>>>>>>>>>>")

    for employee in employees:

        print("\nEmployee ID:", employee["id"])
        print("Employee Name:", employee["name"])
        print("Department:", employee["department"])
        print("Monthly Salary: ₹", employee["salary"])

    print("-----------------------------------------")