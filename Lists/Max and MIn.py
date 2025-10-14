# MAximum and Minimum
nums = [10,2,3,4,4,5,52,90,70]
max_val = nums[0]
min_val = nums[0]
for num in nums:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print(max_val,min_val)