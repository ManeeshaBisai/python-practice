# Stop at a specific number
# Print numbers from 1 to 10, but stop when the number is 5.
for i in range(1,11):
    if i == 5 :
        break
    print(i)

# Skip a specific number
# Print numbers from 1 to 10,but skip 5 using continue.
for i in range(1,11):
    if i == 5 :
        continue
    print(i)