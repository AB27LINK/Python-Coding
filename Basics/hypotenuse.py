# WAP to print the hypotenuse of a triangle(which is right - angled)

import math
perpendicular = float(input("The perpendicular is  : "))
base = float(input("The base is  : "))

hypotenuse = math.sqrt(pow(perpendicular, 2) + pow(base, 2))

print(f"The hypotensue of the triangle is {round(hypotenuse, 4)} cm")