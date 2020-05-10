a = 5
b = 6

print("Before Swap")
print(a)
print(b)

# Swap using Third variable

temp = a
a = b
b = temp

print("After Swap")

print(a)
print(b)

# Swap without using Third variable

a = a + b
b = a - b
a = a - b

print("After Swap")

print(a)
print(b)

# Swap Using XOR

a = a ^ b
b = a ^ b
a = a ^ b

print("After Swap")

print(a)
print(b)


# Swap Using Row TWO

a, b = b, a

print("After Swap")

print(a)
print(b)
