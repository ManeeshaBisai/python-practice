# Check Even or Odd
# Function should tell whether a given integer is even or odd.
def check_even_odd(num):
    r = num % 2
    if r == 0 :
        print("even")
    else :
        print("odd")
num = int(input("enter a num :"))
check_even_odd(num)