# Sort a list without using sort() method

l = [5,2,4,1,0,9]

for i in range(0, len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)