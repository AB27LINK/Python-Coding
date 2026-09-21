# collections : A single "variable" which can store multiple values
# List : [] ordered and changeable. DUPLICATE OK

cars = ["audi", "bmw", "mercedes", "hyundai"]
print(cars)
# for lenth of the list len() is used

#Operation(list)	       Method

# Add item	          append(), insert()
# Remove item	      remove(), pop(), del
# Search	          in, index(), count()
# Sort	              sort()
# Reverse	          reverse()
# Copy                copy()
# Clear	              clear()


# Set : {} unordered and mutable. but ADD/REMOVE OK, no DUPLICATE

cars ={"audi", "bmw", "mercedes", "hyundai"}
print(cars)
# for lenth of the set len() is used

# Task	                           Method

# Add	             add(){only one element}, update(){muliple elements}
# Remove	         remove(), discard(), pop()
# Union	             | , union()
# Intersection	     & , intersection()
# Difference	     - , difference()
# Clear	             clear()

# Tuple : () ordered and unchangeble. DUPLICATES OK, FASTER

cars = ("audi", "bmw", "mercedes", "hyundai")
print(cars)
# for lenth of the tuple len() is used
# We can also use 'in' to check whether element is there or not

# Method	              Use

# count()	        count occurrences
# index()	        find position  