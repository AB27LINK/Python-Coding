# WAP to make a fabbonaci series

n = int(input("Enter a number : "))
a=0
b=1
print(a)
print(b)
for i in range(n-2): # here n-2 is used to make the number of terms desired since two of the terms are already displayed.
    c=a+b
    a=b
    b=c
    print(c)