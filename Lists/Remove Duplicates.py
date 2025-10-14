# Remove Duplicates 
numbers = [1,2,3,4,4,5]
unique = []
for el in numbers :
    if el not in unique:
        unique.append(el)
print(unique)