def calculate_annual_salary(employees):

    emp_id = int(input("Enter Employee ID: "))

    for employee in employees:

        if employee["id"] == emp_id:

            annual_salary = employee["salary"] * 12

            print("\nEmployee Name:", employee["name"])
            print("Monthly Salary: ₹", employee["salary"])
            print("Annual Salary: ₹", annual_salary)

            return

    print("\nEmployee Not Found!")


def calculate_bonus(employees):

    emp_id = int(input("Enter Employee ID: "))

    for employee in employees:

        if employee["id"] == emp_id:

            salary = employee["salary"]

            if salary < 15000:
                bonus = salary * 5 / 100

            elif salary <= 30000:
                bonus = salary * 10 / 100

            else:
                bonus = salary * 15 / 100

            print("\nEmployee Name:", employee["name"])
            print("Monthly Salary: ₹", salary)
            print("Bonus: ₹", bonus)

            return

    print("\nEmployee Not Found!")