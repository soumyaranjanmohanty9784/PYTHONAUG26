# Question 3: Shopping List

with open("shopping_list.txt", "w") as file:

    for i in range(5):
        item = input("Enter Shopping Item: ")
        file.write(item + "\n")


with open("shopping_list.txt", "a") as file:

    for i in range(3):
        item = input("Enter Additional Item: ")
        file.write(item + "\n")

with open("shopping_list.txt", "r") as file:
    print("\nShopping List")
    print(file.read())