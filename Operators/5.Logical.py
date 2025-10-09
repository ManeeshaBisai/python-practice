# Logical operator
# Input a number and check if it is divisible by 2 AND divisible by 3, then check if it is divisible by 2 OR divisible by 3.
num = int(input("enter a num :"))
div1 = (num % 2 == 0 )
div2 = (num % 3 == 0 )
if div1 and div2 :
    print("Divisible by both 2 and 3.")
elif div1 or div2 :
    print("divisible by only one.")
    print(div1,div2)