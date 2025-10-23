# Find factorial of a number
num = int(input("enter a num to find its factorial :"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
    print(fact)