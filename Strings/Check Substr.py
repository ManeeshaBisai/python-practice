# Check Sub strings
# Take two strings and check whether the second string is present inside the first string.
str1 = input("enter some data :")
str2 = input("enter some data :")
if str2.lower() in str1.lower() :
    print("Yes,found")
else:
    print("not,found")