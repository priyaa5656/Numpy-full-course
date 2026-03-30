🧠 1. Array Stacking
👉 Array Stacking means combining multiple arrays into one array.
👉 it creates a new dimension (shape is changed ).

🔹 Example
```python
a = np.array([1,2,3])
b = np.array([4,5,6])
```
👉 both arrays:
a → [1 2 3]
b → [4 5 6]

🔹 Vertical Stacking (vstack)
```python
print(np.vstack((a, b)))
```
🧠 Word-by-word
np.vstack → vertical stacking function
(a, b) → both arrays combined
vertical → top–bottom (rows are added)

👉 Output:
[[1 2 3]
 [4 5 6]]

✔️ it creates 2D array
✔️ 2 rows, 3 columns

🔹 Horizontal Stacking (hstack)
```python
print(np.hstack((a, b)))
```
🧠 Word-by-word
np.hstack → horizontal stacking
horizontal → left–right combine

👉 Output:
[1 2 3 4 5 6]    ✔️ this is 1D array.

row wise / column wise (confusing)

✅ Clear:
vstack → row is added
hstack → columns are extend 

🧠 2. Array Splitting
👉 Array Splitting means dividing one array into multiple smaller arrays.

🔹 Example
```python
c = np.array([[1,2,3], [4,5,6]])
print(c)
```
👉 Output:
[[1 2 3]
 [4 5 6]]

🔹 Horizontal Split (hsplit)
```python
hsplit = np.hsplit(c, 3)
```
🧠 Word-by-word
np.hsplit → horizontal split
c → original array
3 → 3 parts me split

👉 Output (each column are seprated):

[[1]
 [4]]

[[2]
 [5]]

[[3]
 [6]]

✔️ columns are split

🔹 Vertical Split (vsplit)
```python
vsplit = np.vsplit(c, 2)
```

🧠 Word-by-word
np.vsplit → vertical split
2 → 2 parts

👉 Output:
[[1 2 3]]
[[4 5 6]]

✔️ rows are split 

🧠 Important Rule

👉 during Splitting:
✔️ equal division should be possible 

Example:

3 columns → hsplit(c,3) ✔️
2 rows → vsplit(c,2) ✔️
🎯 One-line Summary (Notes 🔥)

👉 vstack → combine vertically (rows)
👉 hstack → combine horizontally (columns)
👉 hsplit → split columns
👉 vsplit → split rows