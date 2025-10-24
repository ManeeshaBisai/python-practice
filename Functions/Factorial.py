# Factorial (using loop)
# Function returns factorial of n using a loop.

def calc_fact(n):
    i = 1
    fact = 1
    while i <= n:
        fact = fact * i
        i += 1
    return fact
n = int(input("enter a num :"))
result = calc_fact(n)
print(result)