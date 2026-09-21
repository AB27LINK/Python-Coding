# nested loop : A loop inside another loop(outer, inner)
#  outer loop:
#       inner loop:

# Writing a simple nested loop to show an example of number printing
"""
for x in range(3) :
    for y in range(1, 10):
        print(y, end="")
    print()
"""
# WAP to make rectangle using * sign only of given rows and column

rows = int(input("Enter the number of rows : "))
column = int(input("Enter the number of columns : "))
symbol = "*"

for x in range(rows) :
    for y in range(column) :
        print(symbol, end="")
    print()