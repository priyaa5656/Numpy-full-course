import numpy as np

# -----------------------------
# Step 1: Creating Arrays
# -----------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)


# -----------------------------
# Step 2: Element-wise Operations
# -----------------------------
print("\nAddition:", np.add(a, b))
print("Subtraction:", np.subtract(a, b))
print("Multiplication:", np.multiply(a, b))
print("Division:", np.divide(a, b))


# -----------------------------
# Dot Product
# -----------------------------
print("\nDot Product:", np.dot(a, b))


# -----------------------------
# Transpose
# -----------------------------

# 1D Array Transpose
print("\nTranspose of a (1D):", a.T)

# 2D Array Transpose
t = np.array([[1, 2, 3],
              [4, 5, 6]])

print("\nOriginal 2D Array:\n", t)
print("\nTransposed Array:\n", t.T)
