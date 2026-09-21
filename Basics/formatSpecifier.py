# Format Specifier : {value : flag} format a value based on what flags are inserted in the f-string
# 1. .(number)f : This flag round of to that many decimal places
# 2. :(number) : Add that many spaces 
# 3. :0(number) : Allocate that many spaces with zero pads
# 4. :< : Left justify
# 5. :> : Right justify
# 6. :^ : Centre allign
# 7. :+ : Use a plus sign to indicate positive values
# 8. := : Place the sign to leftmost position
# 9. : : Insert a space before positive number
# 10. :, : Comma seperator


price1 = 39999.1475

print(f"Price1 is ${price1 : .2f}")
print(f"Price1 is ${price1 :10}")
print(f"Price1 is${price1 :020}")
print(f"Price1 is${price1 :<10}")
print(f"Price1 is${price1 :>10}")
print(f"Price1 is${price1 :^10}")
print(f"Price1 is${price1 :+}")
print(f"Price1 is${price1 :=}")
print(f"Price1 is${price1 : }")
print(f"Price1 is${price1 :,}")