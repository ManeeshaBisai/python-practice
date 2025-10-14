# Sort a list
input = [4,2,1,3]
for i in range(len(input)):
    for j in range(i + 1,len(input)):
        if input[i] > input[j]:
            input[i],input[j] = input[j],input[i]
print(input)