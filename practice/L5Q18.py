# Using only find() write a function that returns True if substring exists
def Substring(s):
    if s.find("in") == 0 or s.find("in") == -1 :
        return False
    else :
        return True
s1 =input("Enter a string : ")
result =Substring(s1)
print(result)