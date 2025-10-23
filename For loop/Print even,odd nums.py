# Print even numbers from 1 to 20
i = 2
for i in range (2,21,2):
    print(i)

# PRint Odd numbers from 1 to 20
i = 1
for i in range(1,20,2):
    print(i)

# 2nd method
for i in range(1,21):
    if i % 2 == 0 :
        print(i)

for i in range(1,21):
    if i % 2 != 0:
        print(i)