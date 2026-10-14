# Count Duplicates in a List

L=list(map(int, input("Enter list elements : ").split()))

dup=[]
for i in L:
    match=0
    for j in L:
        if i==j:
            match=match+1
    if match>1 and i not in dup:
        dup.append(i)

print(dup)