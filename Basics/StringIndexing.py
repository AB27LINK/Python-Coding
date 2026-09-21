# Indexing : accessing the element from the string using [] (indexing operator)
# Formula : [ start : end : step ]

credit_number = "1234-5678-9012-3456"

result = print(credit_number[7])
result1 = print(credit_number[0:4])

# Note : negative indexing is possible which give element from behind the string
result3 = print(credit_number[-2])

# Step [::?] in the formula is to give every "given index" place elements only
result4 = print(credit_number[::3])

# To print the reverse of a string
result5 = print(credit_number[::-1])

result6 = print(credit_number[-1:0])