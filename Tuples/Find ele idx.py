# Find Element Index
# Given a tuple nums = (4, 7, 2, 9, 7, 3), find the index of the first occurrence of 7.
nums = (4, 7, 2, 9, 7, 3)
print(nums.index(7))
first_index = nums.index(7)
second_idx = nums.index(7,first_index + 1)
print(second_idx)