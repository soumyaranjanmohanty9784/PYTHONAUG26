def search_department(employees):

    department = input("Enter Department: ")

    found = False

    print("\nEmployees in", department, "Department:")

    for employee in employees:

        if employee["department"].lower() == department.lower():

            print(employee["name"], "- ₹", employee["salary"])

            found = True

    if found == False:
        print("No Employee Found in this Department!")


def highest_paid_employee(employees):

    if len(employees) == 0:
        print("\nNo Employee Found!")
        return

    highest = employees[0]

    for employee in employees:

        if employee["salary"] > highest["salary"]:

            highest = employee

    print("\n<<<<<<<<<<<<< HIGHEST PAID EMPLOYEE >>>>>>>>>>>>")

    print("Name:", highest["name"])
    print("Department:", highest["department"])
    print("Monthly Salary: ₹", highest["salary"])

    print("-------------------------------------------------")