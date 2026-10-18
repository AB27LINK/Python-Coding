# WAP to make a list in which squares of the even number between 1 to 20

square =[x**2 for x in range(1,21) if x%2==0]
print(square)