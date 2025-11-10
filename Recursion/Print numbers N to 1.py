# Print Numbers N to 1
# print numbers in reverse order using recursion.
def show(n):
    if n == 0:
        return
    print(n)
    show (n - 1)
show(9)