import numpy as np

# -----------------------------
# Array Stacking
# -----------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)

# Vertical Stacking
print("\nVertical Stacking (vstack):")
print(np.vstack((a, b)))

# Horizontal Stacking
print("\nHorizontal Stacking (hstack):")
print(np.hstack((a, b)))


# -----------------------------
# Array Splitting
# -----------------------------
c = np.array([[1, 2, 3],
              [4, 5, 6]])

print("\nOriginal 2D Array:\n", c)

# Horizontal Split
print("\nHorizontal Split (hsplit):")
hsplit = np.hsplit(c, 3)
for s in hsplit:
    print(s)

# Vertical Split
print("\nVertical Split (vsplit):")
vsplit = np.vsplit(c, 2)
for s in vsplit:
    print(s)