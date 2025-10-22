# Sum of first N natural numbers
# Take user input n and find sum = 1+2+3+...+n.
n = int(input("enter nums :"))
i = 1
sum = 0
while i <= n :
    sum = i + sum  
    i += 1
    print(sum)