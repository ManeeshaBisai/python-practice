# Swap two numbers using arithmetic operators
# Swap x and y without using a temporary variable (use + and -).Swap x and y without using a temporary variable (use + and -).

x = int(input("Enter x :"))
y = int(input("Enter y :"))
x = x + y
y = x - y
x = x - y
print("After swapping: x =", x, " y =", y)