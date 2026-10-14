# Find the Smallest Number in the list

nums = list(map(int, input("Enter the numbers : ").split()))

smallest = nums[0]
for i in nums:
    if i < smallest:
        smallest = i

print(smallest)