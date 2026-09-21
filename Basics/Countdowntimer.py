# time.time(): Returns the current time as a floating-point number representing the number of seconds that have elapsed since the epoch. This is useful for measuring time intervals.

# time.sleep(secs): Suspends the execution of the current thread for the number of seconds specified in the argument secs, which can be a float for sub-second precision.

#time.localtime(secs): Converts a time expressed in seconds since the epoch into a struct_time object in local time. If secs is not provided, the current time is used.

# time.gmtime(secs): Similar to localtime(), but converts the time into a struct_time object in UTC (Coordinated Universal Time).

# time.ctime(secs): Converts a time in seconds since the epoch to a 24-character string representing the local time in a human-readable format

# epoch :  when your computer thinks time began (reference point)
# importing time module

import time

timer =int(input("Enter your timer in seconds : "))
# Some other way for reversed timer here is reversed(range(0, timer))
"""
for x in range(timer, 0, -1):
    time.sleep(1)
    seconds = x % 60
    minutes = int(x / 60)% 60
    hours = int(x / 3600)
    print(f"{hours :02}:{minutes :02}:{seconds :02}")
print("Time's Up")

"""
# Writing the same snippet of above code using only while loop

"""
counter = 0
while timer > 0 :
    time.sleep(1)
    print(counter)
    counter += 1
    if counter == timer :
        break
print("Time Up")
"""
# Writing the same while loop with reversed countdown timer

counter = timer
while timer > 0 :
    time.sleep(1)
    seconds = counter % 60
    minutes = int(counter / 60)% 60
    hours = int(counter / 3600)
    print(f"{hours :02}:{minutes :02}:{seconds :02}")
    counter -= 1
    if counter == 0 :
        break
print("Time Up")