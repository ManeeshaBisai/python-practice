# Count vowels in a string
str = input("enter a string:")
count = 0
vowels = "AEIOUaeiou"
for ch in str:
    if ch in vowels:
        count += 1
print(count)