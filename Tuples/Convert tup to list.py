# Convert Tuple to List
# Convert a tuple t = (10, 20, 30) into a list, add a new element 40, then convert it back to tuple.
t = (10, 20, 30)
l = list(t)
l.append(40)
t = tuple(l)
print(t)