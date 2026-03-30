# 📘 Broadcasting in NumPy
👉 Broadcasting is a mechanism that allows operations on arrays of different shapes.
👉 Matlab: bina loop ke arrays ko match karke operation ho jata hai 😎

🔹 Simple samajh
👉 NumPy expand(stretch) array so that shapes match.

## 🔥 Broadcasting Rules 
👉 1. compare shape from right
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
👉 Broadcasting allows operations between arrays of different shapes.

## 🎯 One-line Summary (Notes 🔥)

👉 Broadcasting = different shape arrays ko match karke operation
👉 1 → stretch hota hai
👉 right se comparison hota hai