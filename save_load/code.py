import numpy as np

# 🔹 Create an array
arr = np.array([1, 0, 0, 8])
print("Original Array:")
print(arr)

# 🔹 Save the array to a file
np.save('my_array.npy', arr)
print("\nArray saved as 'my_array.npy'")

# 🔹 Load the array from the file
loaded_arr = np.load('my_array.npy')

print("\nLoaded Array:")
print(loaded_arr)

# 🔹 Verify both arrays are same
print("\nCheck if both arrays are equal:")
print(np.array_equal(arr, loaded_arr))