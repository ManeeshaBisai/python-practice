# Skip vowels in a string
# Take input and print only the consonents(skip vowels)
str = input("enter a string :")
vowels = "AEIOUaeiou"
for char in str:
    if char in vowels:
        continue
    print(char)