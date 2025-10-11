# Replace Word
# Take a sentence and replace a specific word with another word using replace().
sentence = input("enter any sentence :")
old_word = input("Enter the word to replace :")
new_word = input("Enter the new word :")

words = sentence.split()
for i in range(len(words)):
    if words[i] == old_word:
        words[i] = new_word
new_sentence = " ".join(words)
print("updated sentence:",new_sentence)