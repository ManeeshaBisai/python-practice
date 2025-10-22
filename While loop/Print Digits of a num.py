# Print digits of a number (one by one)
num = int(input("enter a num :"))
while num > 0 :
    digit = num % 10 
    print(digit)
    num = num // 10