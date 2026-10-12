# Sum & Average of a List

sum = 0

l=list(map(int, input("Enter a list of numbers : ").split()))

for i in range(0,len(l)):
    sum= sum+l[i]
    avg =sum/len(l)
print(f"The sum is {sum}")
print(f"The average is {avg}")