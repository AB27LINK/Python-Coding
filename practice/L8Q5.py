# WAP for login check

username = "admin"
password = "admin@123"

USER = input("Enter your username : ")
PASS = input("Enter your password : ")

if USER==username and PASS==password:
    print("Login Successful")
else :
    print("Login Credentials Wrong")