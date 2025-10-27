# Count VOwels in a String
# Funtion that counts vowels in a given string.
def count_vowels():
    string = input("enter a string :")
    vowels = "aeiouAEIOU"
    count = 0
    for char in string :
        if char in vowels :
            count += 1
    print(count)
count_vowels()