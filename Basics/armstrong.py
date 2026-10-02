n = int(input("Enter a number : "))
num = n
arm = 0
while n!=0:
    d =n%10
    arm = arm + (d**3)
    n =n//10
if arm == num:
    print("The given value is armstrong")
else :
    print("The given valueis not armstrong")

# Note : / this method gives floating values so we need floor division for integer value