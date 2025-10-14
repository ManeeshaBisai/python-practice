# Repeat Tuple Elements
# Create a tuple (10, 20) and repeat it 3 times using * operator.
tup = (10,20)
result = tup * 3
print(result)

# 2nd method
tup = (10, 20)
result = ()
for _ in range(3):
    result = result + tup
print(result)