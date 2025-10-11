# Remove Spaces from a string
# Remove extra spaces from a string.
s = input("enter data :")
res = ""
for ch in s:
    if ch != " " : 
        res += ch
print("Result:",res)
    