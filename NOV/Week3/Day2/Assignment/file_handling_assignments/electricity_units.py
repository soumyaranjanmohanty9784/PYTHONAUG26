# Question 11: Electricity Bill Calculation

# Write electricity units
with open("electricity_units.txt", "w") as file:

    for i in range(10):

        units = int(input("Enter Household " + str(i + 1) + " Units: "))

        file.write(str(units) + "\n")

# Read units
with open("electricity_units.txt", "r") as file:

    data = file.readlines()

units_list = []

for unit in data:
    units_list.append(int(unit.strip()))

total = sum(units_list)
highest = max(units_list)
lowest = min(units_list)
average = total / len(units_list)

print("\nElectricity Consumption Report")
print("Total Units:", total)
print("Highest Consumption:", highest)
print("Lowest Consumption:", lowest)
print("Average Consumption:", average)