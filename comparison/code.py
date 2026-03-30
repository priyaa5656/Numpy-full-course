import numpy as np

# 🔹 Step 1: Creating Arrays
a = np.array([1, 5, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)

# 🔹 1. Element-wise Comparison
print("\nElement-wise Comparison (a == b):")
print(a == b)   # compares each element at same index

# 🔹 2. Full Array Comparison
print("\nFull Array Comparison (np.array_equal):")
print(np.array_equal(a, b))   # checks if arrays are completely equal

# 🔹 Bonus: Other Comparisons
print("\nGreater than (a > b):")
print(a > b)

print("\nLess than (a < b):")
print(a < b)

print("\nNot equal (a != b):")
print(a != b)