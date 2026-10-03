# WAP to find the sum of the digits of the given number 

n = int(input("Enter a number : "))
sum = 0
while n!=0:
    d=n%10
    sum = sum + d
    n=n//10
print(f"The sum of digits is {sum}")