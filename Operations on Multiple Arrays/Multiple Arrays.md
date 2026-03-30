# 📘 Mathematical Operations on Multiple Arrays
👉 Mathematical operations on multiple arrays mean performing operations between two arrays element-wise.
👉 👉 This means operations are performed on elements at the same index.

🔹 Step 1: Creating Arrays
```python
a = np.array([1,2,3])
b = np.array([4,5,6])
```
🧠 explain:
a → [1 2 3]
b → [4 5 6]
 👉 Both arrays must have the same size. ✔️

🔹 Step 2: Element-wise Operations

## ➕ Addition
```python
print(np.add(a,b))
```
🧠 Word-by-word:
np.add() → addition function
(a,b) → both arrays

👉 Working:
1+4 = 5
2+5 = 7
3+6 = 9
👉 Output:   [5 7 9]

## ➖ Subtraction
```python
print(np.subtract(a,b))
```
👉 Output: [-3 -3 -3]

🧠:
1-4 = -3
2-5 = -3
3-6 = -3

## ✖️ Multiplication
```python
print(np.multiply(a,b))
```
👉 Output: [4 10 18]

🧠:
1×4 = 4
2×5 = 10
3×6 = 18

## ➗ Division
```python
print(np.divide(a,b))
```
👉 Output: [0.25 0.4 0.5]

🧠:
1/4 = 0.25
2/5 = 0.4
3/6 = 0.5

🔥 Important Concept
👉 These are element-wise operations.
👉 This means: same index + same index

## 🔹 Dot Product (Very Important 💥)
👉 Dot product multiplies corresponding elements and then sums them.
```python
print(np.dot(a,b))
```
🧠:  (1×4) + (2×5) + (3×6)
       = 4  +     10 +   18
       = 32

👉 Output:  32

## 🔹 Transpose (T)
👉 Transpose changes rows into columns and columns into rows.

Example 1 (1D array)
```python
print(a.T)
```
👉 Output:  [1 2 3]   👉 No change occurs in a 1D array ❗

Example 2 (2D array)
```python
t = np.array([[1,2,3],
              [4,5,6]])
print(t.T)
```
🧠:
Before:
[[1 2 3]
 [4 5 6]]
(2 rows, 3 columns)

After transpose:
[[1 4]
 [2 5]
 [3 6]]
(3 rows, 2 columns)   👉 👉 Rows and columns are swapped ✔️

## 🎯 One-line Summary (Notes 🔥)
👉 add/subtract/multiply/divide → element-wise
👉 dot → multiply + sum
👉 transpose → rows ↔ columns
