# Stop printing when you find an even number
# From a list of numbers [1, 3, 5, 8, 9, 11], stop when you find the first even number.
nums = [1,3,5,8,9,11]
for num in nums :
    if num % 2 == 0 :
        break
    print(num)