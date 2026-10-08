# Print a 5 by 5 grid skipping the centre
n=int(input("Enter a number of rows : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==3 and j==3:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
# For n=5 only