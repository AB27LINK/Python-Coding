# Username input exercise
# The username must not contain more than 12 characters
# The username must not contain spaces
# The username nust not contain digits

username = input("Enter your username : ")

if len(username) > 12 :
    print("The provided username cannot contain more than 12 characters")
elif not username.count(" ") == 0 :
    print("The provided username cannot contain spaces")
elif not username.isalpha() :
    print("The provided username cannot contain digits")
else :
    print(username)