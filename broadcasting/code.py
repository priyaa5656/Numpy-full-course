import numpy as np

# 🔹 Example 1: 1D + single value
a = np.array([1, 2, 3, 4])
b = np.array([5])

print("Example 1:")
print("Array a:", a)
print("Array b:", b)
print("Result (a + b):", a + b)

# 🔹 Example 2: 2D + 1D
c = np.array([[1, 2, 3],
              [4, 5, 6]])

d = np.array([10, 20, 30])

print("\nExample 2:")
print("Array c:\n", c)
print("Array d:", d)
print("Result (c + d):\n", c + d)