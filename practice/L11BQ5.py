# Most frequent number

bsf=0
l = [1,1,1,1,2,2,3,4,4,4,4,5,4,4,6,6,6,6,4]
bsf =0
max_count=0
for i in range(0,len(l)):
    count=0
    for j in range(0,len(l)):
        if l[i]==l[j]:
            count=count+1
    if max_count<count:
        max_count=count
        bsf=l[i]
print(bsf)
print(max_count)