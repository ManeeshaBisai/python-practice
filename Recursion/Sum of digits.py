# Sum of Digits
# Find the sum of digits of a number using recursion.
def Sum_of_digits(n):
    if n == 0 :
        return 0
    else :
        return (n % 10) + Sum_of_digits(n // 10)
num = int(input("enter a num:"))
print(Sum_of_digits(num))