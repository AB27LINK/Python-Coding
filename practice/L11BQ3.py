# Remove Duplicates (Keep Unique Only)

items = [1,2,2,3,4,4,4,5]
new_list =[]

for i in items:
    if i not in new_list:
        new_list.append(i)

print(new_list)