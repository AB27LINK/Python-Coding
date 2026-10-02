"""
A
AB
ABC
ABCD
ABCDE """

for i in range(6):
    for j in range(i):
        print(chr(65+j),end="")
    print()