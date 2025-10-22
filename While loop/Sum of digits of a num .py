# Find Sum of digits of a number
num = int(input("enter a num :"))
sum = 0
while num > 0 :
    digit = num % 10
    sum = sum + digit
    num //= 10
print(sum)