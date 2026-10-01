# Testing loops
# Synatx of range()
# range(start, stop+1, step)

"""for i in range(1,11,2):
    print(i)"""

# reversed loop
"""for i in reversed(range(0,11,1)):
    print(i)"""

# printing 20 lines "Abhi is Great"
"""for i in range(1,21):
    print("Abhi is Great")"""

# Use of break and continue
# break is used to terminate a loop
# and continue is used to skip a statement (continue ke neeche jo likha hota hai woh uss condition ke liye execute nhi hota.) 

# while loop
# syntax: initialisation 
#         while <condition> :
#               block of statements
#               updation

"""i=int(input("Enter a number : "))
while i<=5:
    if i==4:
        break
    print(i)
    i=i+1
print("END")"""

# WAP to display the table of n upto 10
n= int(input("Enter a number : "))
print(f"Table of {n}")
i=1
while n!=0:
    if i==11:
        break
    print(f"{n} X {i} = {n*i}")
    i=i+1
print("THE END")