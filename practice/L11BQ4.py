# Second Largest Number in the List without using max() and sorting


nums = [23, 8, 12, 89, 45]

l=0
sl=0
for ele in nums:
    if l<ele:
        l=ele
    for el in nums:
        if sl<el and el<l:
            sl=el
        
print(sl)
print(l)
