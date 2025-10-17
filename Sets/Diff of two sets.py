# Difference of Two Sets
# Find elements present in one set but not the other.
a = {1,2,3,4}
b = {3,4,5,6}
result = a.difference(b)
print(result)

a = {1,2,3,4}
b = {3,4,5,6}
result = b.difference(a)
print(result)

print(a - b)
print(b - a)