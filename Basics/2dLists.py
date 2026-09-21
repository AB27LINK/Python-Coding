# 2d Lists : A collection of lists within a list

fruits = ["apple", "banana", "cheeku", "dragonfruit"]
vegetables = ["potatoes", "tomatoes", "pea", "onion"]
meat = ["fish", "elk", "chicken", "beef", "lobster"]

groceries = [fruits, vegetables, meat]
for items in groceries :
    for food in items :
        print(food, end=" ")
    print()