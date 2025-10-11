# Palindrome Check
# Check whether a string reads the same forward and backward.
str = input("enter a word :")
str = str.lower()
i = 0
j = len(str)-1
is_palindrome = True
while i < j :
    if str[i] != str[j] :
        is_palindrome = False
        break
    i += 1
    j -= 1
if is_palindrome:
    print("palindrome")
else:
    print("not palindrome")