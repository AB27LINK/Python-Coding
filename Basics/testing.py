# A testing file for countdown timer
import time

timer =int(input("Enter your timer in seconds : "))
# Some other way for reversed timer here is reversed(range(0, timer))

for x in range(timer, 0, -1):
    time.sleep(1)
    seconds = x % 60
    minutes = int(x / 60)% 60
    hours = int(x / 3600)
    print(f"{hours :02}:{minutes :02}:{seconds :02}")
print("Time's Up")