# Character check
char = input("enter data :")
if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special Character")