# Largest Number in a List
# Function returns the largest value from a non-empty list(use a loop).
def find_largest(list):
    max_val = list[0]
    for x in list :
        if x > max_val :
            max_val = x
    return max_val
list = [23,134,78,500,57,1000,14708]
print("Largest number is :",find_largest(list))