# Stop when "x" is found
# Take string input and print characters until you find "x".
str = input("enter a string :")
for char in str :
    if char == 'x':
        break
    print(char)