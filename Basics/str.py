name = 'Abhinav'
#print(name)

#print(name[-3])

# String slicing
# print(name[0:5:2])

print(name[::-1]) # Reversing the string

# Concatination (+)
new_name = 'W'+ name[1::] # Adding W in place of a in the previous string and creating new string
print(new_name) # There is one more way to change by replace() function

# Repeatition (*)

line = '-'* 30
print(line)
