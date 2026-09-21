# dictionary : A collection of {key : value} pairs
#              ordered and changeable. NO DUPLICATE

capitals = {"India" : "New Delhi",
            "USA" : "Washington DC",
            "Japan" : "Tokyo",
            "UAE" : "Abu Dhabi"}

# print(dir(capitals)) : It helps in giving functions of dictionary

# capitals.get("key") : it gives the value of the key mentioned
print(capitals.get("India"))

# capitals.update({"key" : "value"}) : It adds a key and value pair
capitals.update({"UK" : "London"})
print(capitals)

#capitals.pop("key") : Remove the pair of key and value chosen in the given parenthesis
capitals.pop("USA")
print(capitals)

# capitals.popitem() : It removes the last pair added
capitals.popitem()
print(capitals)

# keys =capitals.keys() : It  gives all the keys present in the dictionary
keys = capitals.keys()
for keys in capitals.keys() :
    print(keys)

# values =capitals.values() : It  gives all the values present in the dictionary
values = capitals.values()
for values in capitals.values() :
    print(values)

# 