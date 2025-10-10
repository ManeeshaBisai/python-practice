# Bitwise Operators
# Input two integers x and y and print x & y, x | y, x ^ y.

x = int(input("enter a num :"))
y = int(input("enter a num :"))
print(x & y)
print(x | y)
print(x ^ y)

#| Bit1 | Bit2 | Bit1 & Bit2 | Bit1 | Bit2 | Bit1 ^ Bit2 |
# ---- | ---- | ----------- | ---- | ---- | ----------- |
# 0    | 0    | 0           | 0    | 0    | 0           |
# 0    | 1    | 0           | 0    | 1    | 1           |
# 1    | 0    | 0           | 1    | 0    | 1           |
# 1    | 1    | 1           | 1    | 1    | 0           |
