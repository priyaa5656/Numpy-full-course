import numpy as np

# 🔹 Step 1: Creating an array with NaN and Inf
data1 = np.array([1, 2, np.nan, 4, np.inf])
print("Original Array:")
print(data1)

# 🔹 Step 2: Check for NaN values
print("\nCheck NaN (np.isnan):")
print(np.isnan(data1))

# 🔹 Step 3: Replace NaN and Inf with finite numbers
print("\nReplace NaN and Inf (np.nan_to_num):")
clean_data = np.nan_to_num(data1)
print(clean_data)

# 🔹 Extra Example 1
arr = np.array([5, np.nan, np.inf])
print("\nExample 1:")
print(arr)
print("After cleaning:", np.nan_to_num(arr))

# 🔹 Extra Example 2 (NaN, +Inf, -Inf)
arr2 = np.array([np.nan, np.inf, -np.inf])
print("\nExample 2:")
print(arr2)
print("After cleaning:", np.nan_to_num(arr2))

# 🔹 Custom replacement
arr3 = np.array([1, np.nan, np.inf])
print("\nCustom Replacement:")
print(arr3)
print(np.nan_to_num(arr3, nan=-1, posinf=999, neginf=-999))