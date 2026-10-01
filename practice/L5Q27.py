# Write a function title_case_words that title cases only words longer than 3 characters.

def title_case_words(s):
    count= len(s)
    if count<=3 :
        print("Titling is not valid on the String")
    else :
        s=s.title()
    return s
s1= input("Enter a String : ")
if len(s1)>3 :
    result = title_case_words(s1)
    print(result)
else :
    print("Titling is not valid on the String")