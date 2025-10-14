# Count Even and Odd
nums = [1,2,3,4,5,6,7]
even = 0
odd = 0
for el in nums:
    if el % 2 == 0 :
        even += 1
    else :
        odd += 1
print("even :",even,"odd :",odd)