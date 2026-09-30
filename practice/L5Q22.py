# Validate a string is a proper title using istitle()

# istitle() is a string method that checks wether the words in the string start with a uppercase letter or not.

s =input("Enter a string : ")
if s.istitle() == True :
    print("String is Valid")
else:
    print("String is Invalid")