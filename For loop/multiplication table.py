# Print the multiplication table of a number
num = int(input("enter a num :"))
for i in range(1,11):
    if i <= 10 :
        print(num,"x",i,"=",i*num)
        i += 1