# WAP for ATM check

amount = int(input("Enter amount you want to withdraw : "))
balance = int(input("Enter amount you have in bank account : "))

if amount<=balance:
    print("Success")
else:
    print("Insufficient balance")