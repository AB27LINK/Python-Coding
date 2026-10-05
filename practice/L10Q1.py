# WAP to print sum of number from 1 to 100

n=int(input("Enter the how many numbers u want to add : "))
sum =0
for i in range(1,n+1):
    sum=sum+i
print(f"Sum of numbers is {sum}")