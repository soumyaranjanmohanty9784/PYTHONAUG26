# Question 5: Search for a Product

products = [
    "Mobile",
    "Laptop",
    "Camera"
    "Keyboard",
    "Headphone",
    "Monitor",
    "Mouse",
    "Speaker",
    "Printer",
    "Tablet",
    
    
]

with open("product_catalog.txt", "w") as file:

    for product in products:
        file.write(product + "\n")

search = input("Enter Product Name: ")

with open("product_catalog.txt", "r") as file:
    data = file.read().splitlines()

count = 0

for product in data:
    if product.lower() == search.lower():
        count += 1

if count > 0:
    print("Product Found")
    print("Product Appears:", count, "Times")
else:
    print("Product Not Found")