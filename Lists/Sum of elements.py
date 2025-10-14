# Sum of Elements
# Input a list of numbers and find the sum of all elements.
elements = [2,1,3,4,7,6,8,9]
total = 0
for nums in elements:
    total += nums
print("Sum of all elements :",total)

# 2nd method
# Step 1: Ask user for input
user_input = input("Enter numbers separated by space: ")

# Step 2: Split the input into a list of strings
numbers_str = user_input.split()  # ['2', '4', '6', '8']

# Step 3: Convert each string into integer using a loop
numbers = []
for num in numbers_str:
    numbers.append(int(num))

# Step 4: Find sum using iteration
total = 0
for num in numbers:
    total += num

# Step 5: Print result
print("Sum of elements:", total)