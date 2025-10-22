# Find factorial of a number
n = int(input("enter a num :"))
fact = 1
i = 1
while i <= n :
    fact = fact * i
    i += 1
    print(fact)