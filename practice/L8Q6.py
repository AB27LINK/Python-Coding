# WAP program that explains or short-circuiting

name = input("Enter your name : ")

if name or name=="":
    print(name or "Guest")

# Here the first true value is being printed due to or short circuit
