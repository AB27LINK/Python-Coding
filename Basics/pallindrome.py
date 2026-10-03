# WAP to check for pallindrome number

n =int(input("Enter a number : "))
num = n
rev =0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
if(num==rev):
    print("The number is pallindrome")
else :
    print("The number is not pallindrome")