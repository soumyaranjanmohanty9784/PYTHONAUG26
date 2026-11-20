from employee_management import (
    add_employee,
    display_employee,
    calculate_annual_salary,
    calculate_bonus,
    search_department,
    highest_paid_employee
)


employees = []


while True:

    print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("     EMPLOYEE MANAGEMENT SYSTEM")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    print("1. Add Employee")
    print("2. Display Employee Details")
    print("3. Calculate Annual Salary")
    print("4. Calculate Employee Bonus")
    print("5. Search Employees by Department")
    print("6. Find Highest-Paid Employee")
    print("7. Exit")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    choice = input("Enter your choice: ")

    if choice == "1":

        employee = add_employee()

        employees.append(employee)

    elif choice == "2":

        display_employee(employees)

    elif choice == "3":

        calculate_annual_salary(employees)

    elif choice == "4":

        calculate_bonus(employees)

    elif choice == "5":

        search_department(employees)

    elif choice == "6":

        highest_paid_employee(employees)

    elif choice == "7":

        print("\nThank You for Using Employee Management System!")

        break

    else:

        print("\nInvalid Choice! Please Try Again.")