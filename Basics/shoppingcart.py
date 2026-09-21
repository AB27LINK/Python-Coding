# WAP to make shopping cart using collections

items = []
prices = []
total = 0

while True :
     item = input("Enter the items to buy (q to quit): ")
     if item.lower() == "q" :
        break
     else :
        price = float(input("Enter the price of the item : $ "))
        items.append(item)
        prices.append(price)

print("-----Item List-----")

for item in items :
    print(item)

for price in prices :
    total += price

print("Your total price for your shopping is : $ {total}")