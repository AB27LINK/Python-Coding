# WAP to display the factors of n
"""n =int(input("Enter a number : "))
for i in range(1,n+1):
    if n%i==0 :
        print(i)"""

# Using while loop
n =int(input("Enter a number : "))
i=1
while i<=n:
    if n%i==0:
        print(i)
        i=i+1
    else :
        i=i+1