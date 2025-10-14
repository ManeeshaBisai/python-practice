# Leap Year 
# Input a year and check if it is a leap year.
year = int(input("Enter year :"))
if year % 400 == 0 or year % 4 == 0 :
    print("leap year")
else :
    print("not leap year")