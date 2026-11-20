# Question 7: File Management Menu

import os

while True:

    print("\n===== COMPANY PROFILE MENU =====")
    print("1. Create File")
    print("2. Write Company Information")
    print("3. Read File")
    print("4. Append Details")
    print("5. Rename File")
    print("6. Delete File")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        with open("company_profile.txt", "w") as file:
            print("File Created Successfully!")

    elif choice == "2":

        name = input("Enter Company Name: ")
        location = input("Enter Location: ")

        with open("company_profile.txt", "w") as file:
            file.write("Company Name: " + name + "\n")
            file.write("Location: " + location + "\n")

        print("Information Written Successfully!")

    elif choice == "3":

        if os.path.exists("company_profile.txt"):
            with open("company_profile.txt", "r") as file:
                print(file.read())
        else:
            print("File Not Found!")

    elif choice == "4":

        details = input("Enter New Company Details: ")

        with open("company_profile.txt", "a") as file:
            file.write(details + "\n")

        print("Details Added Successfully!")

    elif choice == "5":

        if os.path.exists("company_profile.txt"):
            os.rename("company_profile.txt", "business_profile.txt")
            print("File Renamed Successfully!")
        else:
            print("File Not Found!")

    elif choice == "6":

        if os.path.exists("business_profile.txt"):
            os.remove("business_profile.txt")
            print("File Deleted Successfully!")

        elif os.path.exists("company_profile.txt"):
            os.remove("company_profile.txt")
            print("File Deleted Successfully!")

        else:
            print("File Not Found!")

    elif choice == "7":

        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")