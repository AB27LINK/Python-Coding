# Print

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5
"""
n=int(input("Enter a number of rows : "))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
    num=num+1
    print()