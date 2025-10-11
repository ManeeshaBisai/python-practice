# Count words in a sentence
# Count number of words in a sentence.
s = input("enter a sentence :")
count = 0
in_word = False
for ch in s:
    if ch != " " and in_word == False :
        count += 1
        in_word = True
    elif ch == " " :
        in_word = False
print(count)
