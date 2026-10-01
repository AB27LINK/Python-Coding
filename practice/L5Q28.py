# Given a list of names with inconsistent spacing and casing, normalize each name.

names =(input("Enter names : ").split())
for i in range(len(names)) :
    names[i]= names[i].title()
print(names)