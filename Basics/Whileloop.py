# While loop : Execute some code WHILE some condition remains true

name = input("Enter your name : ")

while name == "" :
    print("You have not given your name until now")
    name = input("Enter your name : ")

print(f"You are {name}")


num = int(input("Enter a number between 1 to 10 : "))

while num<1 or num>10 :
    print("Invalid input")
    num = int(input("Enter a number between 1 to 10 : "))

print(f"Your given number is {num}")

