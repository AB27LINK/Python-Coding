# Write a function that counts the number of vowels in a string using count() for each vowel.

def vowels(s):
    s=s.lower()
    a=s.count("a")
    e=s.count("e")
    i=s.count("i")
    o=s.count("o")
    u=s.count("u")
    counter=a+e+i+o+u
    return counter
s1 =input("Enter a string : ")
result = vowels(s1)
print(result)