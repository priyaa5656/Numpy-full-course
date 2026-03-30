import numpy as np

# -----------------------------
# 1D ARRAY
# -----------------------------
a = np.array([1, 3, 5, 7, 9])
print("Array:", a)

# Indexing
print(a[0])   # first element
print(a[4])   # fifth element
print(a[-1])  # last element

# Slicing
print(a[0:3])   # first 3 elements
print(a[-3:])   # last 3 elements
print(a[1:4])   # middle elements
print(a[0::2])  # alternate elements


# -----------------------------
# 2D ARRAY
# -----------------------------
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("\n2D Array:\n", arr2)

# Row access
print(arr2[0])  # first row
print(arr2[1])  # second row

# Element access
print(arr2[0][0])  # row 0, column 0
print(arr2[1][2])  # row 1, column 2

# 2D Slicing
print(arr2[:, 0])   # first column
print(arr2[:, 1])   # second column
print(arr2[:, 2])   # third column
print(arr2[0, :])   # first row
print(arr2[:, 1:])  # sub-matrix


# -----------------------------
# 3D ARRAY
# -----------------------------
arr3 = np.array([
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
])

print("\n3D Array:\n", arr3)

# Row access
print(arr3[0][0])  # first row
print(arr3[0][2])  # third row

# Element access
print(arr3[0][0][2])  # element 3
print(arr3[0][2][2])  # element 9

# Column slicing
print(arr3[:, :, 0])  # first column
print(arr3[:, :, 1])  # second column
print(arr3[:, :, 2])  # third column

# Advanced slicing
print(arr3[:, :, 1:2])    # second column
print(arr3[:, 2:, 1:2])   # last row + second column
