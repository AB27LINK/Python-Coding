# The Copy Trap

original = [1, 2, 3]
backup = original.copy()

backup.append(99)
print(original)
print(backup)