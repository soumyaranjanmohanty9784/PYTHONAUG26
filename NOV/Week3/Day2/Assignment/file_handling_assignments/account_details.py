# Question 12: User Login System

# Registration
username = input("Enter Username: ")
email = input("Enter Email: ")
password = input("Enter Password: ")

# Save account details
with open("account_details.txt", "w") as file:

    file.write(username + "\n")
    file.write(email + "\n")
    file.write(password + "\n")

print("\nRegistration Successful!")

# Login
print("\n===== LOGIN =====")

login_username = input("Enter Username: ")
login_email = input("Enter Email: ")
login_password = input("Enter Password: ")

# Read saved details
with open("account_details.txt", "r") as file:

    data = file.readlines()

saved_username = data[0].strip()
saved_email = data[1].strip()
saved_password = data[2].strip()

# Check credentials
if (login_username == saved_username and
    login_email == saved_email and
    login_password == saved_password):

    print("Login Successful!")

else:
    print("Invalid Credentials!")