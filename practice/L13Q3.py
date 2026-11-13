#  Unique Word Counter

s =input("Enter a Sentence: ")
s1= s.split()
c=0
s1= set(s1)
for i in range(0, len(s1)):
    c=c+i
print(c)