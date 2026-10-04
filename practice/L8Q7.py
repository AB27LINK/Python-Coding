# WAP which shows distinction between == and is

l=[1,2,3,4]
l1=[1,2,3,4]

if l1==l:
    print("True")
else :
    print("False")
if l1 is l:
    print("True")
else :
    print("False")


# == compares values while is compares object