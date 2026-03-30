🧠 1. Reshape Array
👉 Reshape is used to change the shape (rows and columns) of an array without changing its data.

🔹 Example
```python
arr1 = np.array([1,2,3,4,5,6])
print(arr1)
```
👉 Output:
[1 2 3 4 5 6]

🧠 Important Correction ❗
shape (1,6)
means 👉 this actually (6,) --> (1D array)

🔹 Reshape to (6,1)
```python
reshaped = arr1.reshape((6,1))
print(reshaped)
```
🧠 Word-by-word
arr1 → original array
.reshape() → shape change function
(6,1) → 6 rows, 1 column

👉 Output:

[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]

✔️ now it is 2D array.

🔹 Reshape to (2,3)
```python
reshaped2 = arr1.reshape((2,3))
print(reshaped2)
```
🧠 explain
(2,3) → 2 rows, 3 columns
👉 6 elements = 2×3 ✔️

👉 Output:
[[1 2 3]
 [4 5 6]]

🧠 Important Rule
👉 Total elements same hone chahiye
Original = 6 elements  
New shape = rows × columns = 6 ✔️


📘 2. Flatten Array
👉 Flatten converts a multi-dimensional array into a 1D array.

🔹 Example
```python
print(reshaped2.flatten())
```
🧠 Word-by-word
reshaped2 → 2D array
.flatten() → 1D me convert

👉 Output:
[1 2 3 4 5 6]


🎯 One-line Summary (Notes 🔥)
👉 reshape → change shape (same data)
👉 flatten → convert to 1D