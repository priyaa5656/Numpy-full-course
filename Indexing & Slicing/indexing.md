📘 Indexing & Slicing in NumPy
👉 Indexing is used to access specific elements of an array.
👉 Slicing is used to access a range (multiple elements) from an array.

💡 Simple:
Indexing → find one value 
Slicing → find multiple values 


🔹 1. 1D Array Indexing
👉 1D array indexing is used to access a single element from a one-dimensional array using its position (index).

```python
a = np.array([1,3,5,7,9])
print(a)
```
👉 Output:
[1 3 5 7 9]


🔍 what is Index?
👉 👉 Each element has a specific position called an index.

Value:   1   3   5   7   9
Index:   0   1   2   3   4


🔍 Negative Indexing
👉 Last se count hota hai:

Value:   1   3   5   7   9
Index:  -5  -4  -3  -2  -1 
✔️ Index always starts from 0.


🔍 How to access an element?

Example 1.
```python
print(a[0])
```
🧠 
a → array
[0] → index (position)
indexing 0 se start hoti hai

👉 Output:  1

Example 2.
```python
print(a[4])
```
👉 Output:  9

Example 3.
✔️ 5th element (index = 4)

```python
print(a[-1])
```
👉 Output: 9
🧠 Samajh:
-1 → last element
-2 → second last


🔹 2. Slicing (1D Array)
👉 Slicing is used to access multiple elements from an array using a range of indices.
🧠 Syntax
array[start : stop : step]
🔍 Rule
start → where to start from
stop → up to where (❗ not included)
step → gap (how much to skip)gap

Example 1
```python
print(a[0:3])
```
👉 Output:  [1 3 5]    ✔️ index 0,1,2 (3 is not included)

Example 2
```python
print(a[-3:])
```
👉 Output:      [5 7 9]  ✔️ last 3 elements

Example 3
```python
print(a[1:4])
```
👉 Output:   [3 5 7]

Example 4
```python
print(a[0::2])
```
👉 Output:    [1 5 9]  ✔️ every 2nd element



🔹 3. 2D Array (Matrix)
👉 A 2D array is a collection of elements arranged in rows and columns (like a table or matrix).
```python
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2)
```
👉 Output:
[[1 2 3]
 [4 5 6]]


👉 Indexing in 2D array = [row, column]
       Column 
        0  1  2
Row 
  0    [1  2  3]
  1    [4  5  6] 

🔍 Row access  [0] means 0th row  ,[1] means 1th row
Example 1. 

```python
print(arr2[0])   
```
👉 Output: [1 2 3] ✔️ first row

Example 2. 

```python
print(arr2[1])
```
👉 Output:  [4 5 6]


🔍 Row with coloum access  [0][0] means 0th row with 0th coloum ,[1][2] means 1st row with 2 column
Example 3. 

```python
print(arr2[0][0])
```
👉 Output:  1  ✔️ row 0, column 0

Example 4.

```python
print(arr2[1][2])
```
👉 Output:  6 ✔️ row 1, column 2


🔹 2D Slicing
👉 2D slicing is used to access multiple elements from a 2D array using row and column ranges.
syntax:--

array[row_start:row_end , col_start:col_end]
👉 Indexing in 2D array = [row, column]
       Column 
        0  1  2
Row 
  0    [1  2  3]
  1    [4  5  6] 

Example 1. 
```python
print(arr2[:, 0])
```
👉 Output:  [1 4]
🧠 Samajh:
: → sab rows
0 → first column

Example 2. 
```python
print(arr2[:, 1])
```
👉 Output: [2 5]

Example 3.
```python
print(arr2[:, 2])
```
👉 Output:  [3 6]

Example 4.
```python
print(arr2[0, :])
```
👉 Output:  [1 2 3]

Example 5. 
```python
print(arr2[:, 1:])
```
👉 Output:
[[2 3]
 [5 6]]



🔹 4. 3D Array
👉 A 3D array is a collection of 2D arrays (layers), arranged in three dimensions.
```python
arr3 = np.array([
 [[1,2,3],
 [4,5,6],
 [7,8,9]]
])
```
👉 Output:

[[1 2 3]
 [4 5 6]
 [7 8 9]]

🔍 Row access
Example 1.
```python
print(arr3[0])
```
👉 Output:  [1 2 3]

Example 2.
```python
print(arr3[2])
```
👉 Output:   [7 8 9]


🔍 Element access
Example 3.
```python
print(arr3[0][2])
```
👉 Output:  3
Example 4.
```python
print(arr3[2][2])
```
👉 Output:  9


🔹 Column slicing (important 🔥)
Example 5.
```python
print(arr3[:, 0])
```
👉 Output: [1 4 7]
Example 6.
```python
print(arr3[:, 1])
```
👉 Output:  [2 5 8]
Example 7.
```python
print(arr3[:, 2])
```
👉 Output:[3 6 9]


🔹 Advanced slicing
Example 8.
```python
print(arr3[:, 1:2])
```
👉 Output:
[[2]
 [5]
 [8]]
✔️ second column
Example 9.
```python
print(arr3[2:, 1:2])
```
👉 Output:   [[8]]  ✔️ last row + second column

| Concept  | Meaning            |
|----------|--------------------|
| indexing | single element     |
| slicing  | multiple elements  |
| 1D       | [index]            |
| 2D       | [row, column]      |
| :        | all values         |
| step     | gap                |
