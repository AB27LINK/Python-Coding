# WAP to change if elif else into match-case

num = int(input("Enter a number : "))
match num:
    case 0:
        print("Number is 0")
    case _ if num > 0:
        print("Number is positive")
    case _:
        print("Number is negative")
