# Check Element
numbers = [1,2,3,4]
target = 3
found = False
for num in numbers :
    if num == target :
        found = True
        break
if found:
    print("present")
else :
    print("not present")