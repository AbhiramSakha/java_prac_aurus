#Operators in java
a = 10
b = 20
# Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)
print("Modulus:", b % a)
# Relational Operators
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", b > a)
print("Less than:", a < b)
print("Greater than or equal to:", b >= a)
print("Less than or equal to:", a <= b)
# Logical Operators
print("Logical AND:", (a < b) and (b > 5))
print("Logical OR:", (a > b) or (b > 5))
print("Logical NOT:", not(a < b))
# Assignment Operators
c = a
print("Assignment:", c)
c += b
print("Addition Assignment:", c)
c -= a
print("Subtraction Assignment:", c)
c *= 2
print("Multiplication Assignment:", c)
c /= 2
print("Division Assignment:", c)
c %= 3
print("Modulus Assignment:", c)
# Increment and Decrement Operators
a += 1
print("Increment:", a)
b -= 1
print("Decrement:", b)
# Bitwise Operators
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", b >> 1)
# Ternary Operator
max_value = a if a > b else b
print("Ternary Operator (Max Value):", max_value)
# Type Comparison Operator
print("Type Comparison:", isinstance(a, int))
# instanceof operator is not directly available in Python, but we can use isinstance() function
