# Skip the multiple of 3 between 1-20

for i in range(1,21):
    if i%3==0:
        continue
    else:
        print(i)