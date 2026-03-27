📘 NumPy Array Attributes

What is array attributes?
👉 Array Attributes are properties of a NumPy array that describe its structure, size, data type, and dimensions.
or
👉 “Attributes describe the nature of the array. (shape, size, type, dimension)”

🔹 Array making
```python
arr1 = np.array([[1,2,3], [4,5,6]])
print(arr1)
```
👉 Output:
[[1 2 3]
 [4 5 6]]

✔️this is 2D array (matrix)
✔️ 2 rows, 3 columns


🔍 1. Shape
🧠 Definition: 👉 Shape indicates how many rows and columns are in the array.
```python
print("Shape", arr1.shape) 
```

👉 Output:
Shape (2, 3)
2 → rows  , 3 → columns   ✔️ Means: 2 rows × 3 columns


🔍 2. Size
🧠 Definition: 👉Size tells total number of elements in array
```python
print("Size", arr1.size)
```
👉 Output:
Size 6
👉 Elements: 1,2,3,4,5,6 → total 6  ✔️ thats why size = 6


🔍 3. dtype (Data Type)
🧠 Definition: 👉 dtype indicates what is data type of the array's elements.
```python
print("dType", arr1.dtype)
```
👉 Output:
dType int64
👉 all values are integer  ✔️ so type = int64

🔍 4. ndim (Number of Dimensions)
🧠 Definition: 👉 ndim indicates how many dimensions the array has.
```python
print("n_dim", arr1.ndim)
```
👉 Output:
n_dim 2
👉 this is 2D array (rows + columns)

