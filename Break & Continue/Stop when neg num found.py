# Stop when negative number found
# Given numbers [3, 5, 7, -1, 4, 6], stop printing when a negative number appears.
nums = [3,5,7,-1,4,6]
for num in nums:
    if num < 0 :
        break
    print(num)