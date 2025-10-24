# Skip words shorter than 4 letters
# Given words = ["I", "love", "my", "India"], print only words with 4 or more letters.
words = ["I", "love", "my", "India"]
for word in words:
    if len(word) < 4 :
        continue
    print(word)