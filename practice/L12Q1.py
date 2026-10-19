# Uppercase the Long Words

words = ["hi", "python", "ok", "comprehsion", "go"]
upper = [w.upper() for w in words if len(w)>2]

print(upper)