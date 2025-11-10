# Print Numbers 1 to N
# Print numbers from 1 to n recursively.
def print_nums(i,n):
    if i > n:
        return
    print(i)
    print_nums(i+1,n)
print_nums(1,9)