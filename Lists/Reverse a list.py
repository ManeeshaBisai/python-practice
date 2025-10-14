# Reverse a list
num = [1,2,3]
rev = []

for i in range (len(num)-1,-1,-1):
    rev.append(num[i])

print(rev)