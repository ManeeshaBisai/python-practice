# Skip multiples of 3
# Print numbers from 1-15,but skip all multiples of 3.
for i in range(1,15):
    if i % 3 == 0 :
        continue
    print(i)