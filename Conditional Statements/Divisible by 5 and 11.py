# Divisible by 5 and 11
num = int(input("enter a num :"))
if num % 5 == 0 and num % 11 == 0 :
    print("Divisible by both")
elif num % 5 == 0 or num % 11 == 0 :
    print("Divisible by one")
else :
    print("Not divisible by 5 or 11")