# Stop when sum exceeds 15
# Add numbers from [2, 4, 3, 5, 7]. Stop if total sum exceeds 15.
nums = [2,4,3,5,7]
sum = 0
for num in nums:
    sum = sum + num
    if sum > 15 :
        break
    print(sum)