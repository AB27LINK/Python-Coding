#Print
"""
A
A B
A B C
A B C D
A B C D E
"""
n=int(input("Enter a number of rows : "))
for i in range(n+1):
    for j in range(i):
        a=65+j
        print(chr(a),end=" ")
    print()