# Question 9: Product Inventory (CSV)

import csv

# Write CSV file
with open("inventory.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Product ID", "Product Name", "Category", "Price", "Quantity"])

    for i in range(5):

        print("\nEnter Product", i + 1, "Details")

        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        price = input("Enter Price: ")
        quantity = input("Enter Quantity: ")

        writer.writerow([pid, name, category, price, quantity])

# Read CSV file
with open("inventory.csv", "r") as file:

    reader = csv.reader(file)

    print("\nProduct Inventory")

    for row in reader:
        print(row)