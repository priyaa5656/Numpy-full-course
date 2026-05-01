# 📘 Broadcasting in NumPy
👉 Broadcasting is a mechanism that allows NumPy to perform element-wise operations on arrays of different shapes by automatically expanding the smaller array.

🔹 Simple 
👉 NumPy expands (stretches) arrays so that shapes match.

## 🔥 Broadcasting Rules 
👉 1. Compare shapes from right to left
example:
(2,3)
(1,3)

👉 2. Dimensions must be the same or one of them should be 1.
👉 3. If an array has fewer dimensions, add 1 on the left.
👉 4. Any dimension equal to 1 can be stretched.

🔹 Example 1 (1D + single value)
```python
a = np.array([1,2,3,4])
b = np.array([5])
print(a + b)
```
🧠:
a → [1 2 3 4]
b → [5]
👉 NumPy internally:
b → [5 5 5 5]
👉 Addition:
[1 2 3 4] + [5 5 5 5]
= [6 7 8 9]


🔹 Example 2 (2D + 1D array)
```python
c = np.array([[1,2,3],
              [4,5,6]])
d = np.array([10,20,30])
print(c + d)
```
🧠 Shapes:
c → (2,3)
d → (3,) → becomes (1,3)
👉 NumPy internally:
d →
[10 20 30]
[10 20 30]
👉 Addition:
[1 2 3] + [10 20 30] = [11 22 33]
[4 5 6] + [10 20 30] = [14 25 36]
👉 Final Output:
[[11 22 33]
 [14 25 36]]

## 🔥 Important Concept (Gold Line ⭐)
👉 👉 Broadcasting = automatic expansion of smaller array

## 🎯 One-line Summary (Notes 🔥)

👉 Broadcasting → Operation by matching different shape arrays
👉 Smaller array → automatically stretches
👉 Comparison → from right 