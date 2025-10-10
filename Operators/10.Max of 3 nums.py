# Maximum of three numbers using operators
# Input three numbers and find the largest using comparison operators.

x = int(input("Enter a 1st num :"))
y = int(input("Enter a 2nd num :"))
z = int(input("Enter a 3rd num :"))

if x > y and x > z :
    print(x,"is largest of three nums.")
elif x < y and y > z :
    print(y,"is largest of three nums.")
else:
    print(z,"is largest of three nums.")