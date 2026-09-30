# Write a function that remove all extra spaces from a string and join

def remove(s) :
    s=s.strip()
    s=s.split()
    return " ".join(s)
s1 =input("Enter a String : ")
result = remove(s1)
print(s1)