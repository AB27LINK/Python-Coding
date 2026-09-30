# Split on "::" and rejoin withg "|"
s ="a::b::c"
s1 =s.split("::")
print("|".join(s1))