# Sum of first 10 Natural Numbers
# Write a function that returns the sum 1 + 2 + ... + 10 (use a loop).
def sum_natural_nums():
    total = 0
    for i in range(1,11) :
        total = total+ i
    print(total)
sum_natural_nums()