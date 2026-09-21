# for loop : It execute a block of code  fixed number  of times
# It iterate over a range, strings, sequence etc.

# Here x is a counter variable

# A loop to count from 1 to 10
for x in range(1, 11) :
    print(x)

# A loop to count reverse from 10 to 1
for y in reversed(range(1, 11)) :
    print(y)

print("HAPPY NEW YEAR")

# A loop to iterate a string
name = "ABHI"

for z in name :
    print(z)

# A loop to explain continue and break keyword here we will print from 1 to 20 but skip over number 13 (for eg)
for num in range(1, 21) :
    if num == 13 :
        continue
    else :
        print(num)

# break : A keywork used to break a code or break the loop in between
# continue : A keyword to skip over a element in a loop