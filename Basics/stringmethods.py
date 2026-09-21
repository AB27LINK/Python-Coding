# string methods in python that can help in doing some specific operations

# 1. len() : It gives the length of the string given by the user
# 2. variable(that is string here).find() : It finds the index of a character (which is the first occurence) in a string given
# 3. variable(that is string here).rfind() : It finds the index of a character (which is the last occurence) in a string given
# 4. variable(that is string here).capitalize() : It capitalize the first letter of the string
# 5. variable(that is string here).upper() : It converts the given string into uppercase
# 6. variable(that is string here).lower() : It converts the given string into lowercase
# 7. variable(that is string here).isdigit() : It checks whether the string given is digits only or not (it gives the output in boolean)
# 8. variable(that is string here).isalpha() : It checks whether the string given is alphabets only or not (it gives the output in boolean)
# 9. variable(that is string here).count() : It count the occurence of the given character in the string 
# 10. variable(that is string here).replace( , ) : It replaces the character chosen with another character in the string


name = input("Enter your name : ")

result = len(name)
print(result)

result1 = name.find("A")
print(result1)

result2 = name.rfind("a")
print(result2)

result3 = name.count("a")
print(result3)

name = name.replace("a", "i")
print(name)