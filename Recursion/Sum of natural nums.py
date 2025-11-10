# Sum of Natural Numbers
# Find sum of first n numbers using recursion.
def Sum_nums(n):
    if n == 0 :
        return 0
    else :
        return n + Sum_nums(n-1)
print(Sum_nums(7))