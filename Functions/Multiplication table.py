# Multiplication Table of Given Number
# Function that prints multiplication table of n from 1 to 10.
def calc_table_nums(n):
    for i in range(1,11):
        print(n,"x",i,"=",n * i)
n = int(input("enter a num :"))
calc_table_nums(n)