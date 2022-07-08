from getpass import getpass

username = input("Enter Your Username: ")
password = getpass("Enter Your Password: ")

if username == "pourya" and password == "pourya is very sensetive":
    print("Login Successfully.")
else:
    print("Username or Password Wrong.")

