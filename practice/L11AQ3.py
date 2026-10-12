# Find the largest number

L=list(map(int, input("Enter the list elements : ").split()))
largest = L[0]

for i in range(0,len(L)):
    if L[i]>largest:
        largest=L[i]
print(largest)