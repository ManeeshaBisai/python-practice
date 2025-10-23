# Stop printing when you find an even number
# From a list of numbers [1, 3, 5, 8, 9, 11], stop when you find the first even number.
nums = [1,3,5,8,9,11]
for num in nums :
    if num % 2 == 0 :
        break
    print(num)

# Skip even numbers
# Print all odd numbers between 1 to 10 using continue.
for num in range(1,10):
    if num % 2 == 0:
        continue
    print(num)