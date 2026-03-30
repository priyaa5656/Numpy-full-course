import numpy as np

# -----------------------------
# Original Array
# -----------------------------
arr1 = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:", arr1)


# -----------------------------
# Reshape (6,1)
# -----------------------------
reshaped = arr1.reshape((6, 1))
print("\nReshape (6,1):\n", reshaped)


# -----------------------------
# Reshape (2,3)
# -----------------------------
reshaped2 = arr1.reshape((2, 3))
print("\nReshape (2,3):\n", reshaped2)


# -----------------------------
# Flatten
# -----------------------------
flat = reshaped2.flatten()
print("\nFlattened Array:", flat)