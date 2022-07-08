from getpass import getpass

username = input("Enter Your Username: ")
password = getpass("Enter Your Password: ")


if username == "amjad" and password == "maktab78":
   pass
if username == "asghar" and password == "maktab78":

    print("Login Successfully.")
else:
    print("Username or Password Wrong.")

