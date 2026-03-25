import numpy as np

# Version check
print("NumPy Version:", np.__version__)

# 1. List
list1 = [1, 2, 3]
print("List:", list1)

# 2. Convert to NumPy array
arr_list1 = np.array(list1)
print("Array:", arr_list1)

# Type check
print("Type:", type(arr_list1))

# Dimension check
print("Dimension:", arr_list1.ndim)

# 3. 2D Array
list2 = [4, 5, 6]
arr_list1_2 = np.array([list1, list2])
print("\n2D Array:\n", arr_list1_2)

# 2D dimension
print("2D Dimension:", arr_list1_2.ndim)

# 4. 3D Array
list3 = [7, 8, 9]
arr_list1_3 = np.array([[list1, list2, list3]])
print("\n3D Array:\n", arr_list1_3)

# 3D dimension
print("3D Dimension:", arr_list1_3.ndim)
