# Count Prime in Range

r=int(input("Enter the range  : "))
count=0
for i in range(0,r):
    prime = 1
    if i<2:
        continue
    for j in range(2,i):
        if i%j==0:
            prime = 0
            break
    if prime == 1:
        count+=1
        print(i)
print(f"The number of prime between the range is {count}")