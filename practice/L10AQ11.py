# Print right aligned star triangle

"""
    *
   **
  ***
 ****
*****
"""
n=int(input("Enter a number of rows : "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()