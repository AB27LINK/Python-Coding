# WAP to check prime number
# A basic new idea
"""n =int(input("Enter a number : "))
c=0
for i in range(1,n+1):
    if n%i==0 :
        c=c+1
if c==2:
    print("The number is prime")
else:
    print("Not a prime number")"""
# Optimal solution which give O(root n) Time Complexity
n = int(input("Enter a number: "))

if n < 2:
    print("Not a prime number")
else:
    c = 0

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            c += 1

    if c == 1:
        print("The number is prime")
    else:
        print("Not a prime number")