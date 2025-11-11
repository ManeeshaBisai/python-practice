# Fibonacci Series
# Print Fibonacci series up to n terms.
def fib(n):
    if n == 0:
        return 0       # base case 1
    elif n == 1:
        return 1       # base case 2
    else:
        return fib(n-1) + fib(n-2)   # recursive relation
for i in range(6):
    print(fib(i))