import numpy as np

# 🔹 Step 1: Creating Array
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", a)

# 🔹 1. Sum
print("\nSum:", np.sum(a))   # total of all elements

# 🔹 2. Mean (Average)
print("Mean:", np.mean(a))   # average value

# 🔹 3. Median
print("Median:", np.median(a))   # middle value

# 🔹 4. Standard Deviation
print("Standard Deviation:", np.std(a))   # spread of data

# 🔹 5. Minimum
print("Minimum:", np.min(a))   # smallest value

# 🔹 6. Maximum
print("Maximum:", np.max(a))   # largest value