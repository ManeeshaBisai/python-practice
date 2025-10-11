# Count Vowels
# Take a string and count how many vowels are in it.
str = input("enter a string :")
vowels = "AEIOUaeiou"
count = 0
for char in str :
    if char in vowels :
        count = count + 1
print("number of vowels :",count)