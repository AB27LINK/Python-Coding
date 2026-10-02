# WAP to dispaly the factorial of a number

n= int(input("Enter a number : "))
num = n
fac=1
if n==0:
    print("1")
else :
    while n>0:
        fac=fac*n
        n=n-1
print(f"The factorial of {num} is {fac}")