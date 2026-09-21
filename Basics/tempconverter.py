# WAP to convert temperature from C to F and F to C

import math

unit = input("The unit to be converted (C or F) : ")
temp = float(input("The temperature to be converted is : "))

if unit == "C":
    result = (temp*(9/5)) + 32
    print(f"The converted temperature is {result}")
elif unit == "F":
    result = (temp - 32)*(5/9)
    print(f"The converted temperature is {result}")
else :
    print("The given unit is invalid")