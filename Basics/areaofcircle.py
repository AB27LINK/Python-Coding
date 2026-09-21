# WAP to print the area of a circle

import math

radius = float(input("Enter the readius of the circle : "))
area = math.pi* pow(radius, 2)

print(f"The area Of circle is {round(area, 4)} cm²")