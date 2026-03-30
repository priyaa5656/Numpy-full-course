# 📘 Mathematical Operations on NumPy Array
##🧠 1. Why NumPy over List?
👉 NumPy arrays are faster than Python lists because operations are performed in optimized C code internally.
👉 NumPy arrays are also faster because they perform operations on the entire array at once (vectorization), while lists use loops.

🔹 Example (Speed comparison)
❌ Python List (Slow 🐢)
```python
numbers = list(range(1, 100000001))
result = [x + 5 for x in numbers]
```
👉 Explanation:
Python uses a loop
Each element is processed one by one
Takes more time

✅ NumPy Array (Fast 🚀)
```python
numbers = np.arange(1, 100000001)
result = numbers + 5
```
👉 Explanation:
NumPy uses vectorization
All elements are processed at once
Takes less time

🧠 2. Basic Mathematical Operations
👉 Mathematical operations can be directly applied on NumPy arrays element-wise.

🔹 Example
```python
a = np.array([10, 20, 40, -30])
print(a)
```
👉 Output:   [10 20 40 -30]

🔹 Addition
```python
print(a + 10)
```
🧠 Word-by-word:
a → array
+10 → adds 10 to each element

👉 Output: [20 30 50 -20]

🔹 Subtraction
```python
print(a - 30)
```
👉 Output:   [-20 -10 10 -60]

🔹 Multiplication
```python
print(a * 2)
```
👉 Output:   [20 40 80 -60]

🔹 Division
```python
print(a / 10)
```
👉 Output:
[ 1.  2.  4. -3.]  ✔️ Note: The Output is in float. 

🧠 3. Advanced Functions
🔹 Square
👉 np.square() returns the square of each element in the array.
```python
b = np.array([1, 4, 9])
print(np.square(b))
```
👉 Output: [ 1 16 81]

🔹 Square Root
👉 np.sqrt() returns the square root of each element in the array.
```python
print(np.sqrt(b))
```
👉 Output:   [1. 2. 3.]

🧠 4. Trigonometric Functions (HW 🔥)
👉 Trigonometric functions apply sin, cos, tan to each element (in radians).
👉 all of these function work in the same way.
```python
print(np.sin(b))
print(np.cos(b))
print(np.tan(b))
```


🎯 One-line Summary (Notes 🔥)
👉 NumPy operations = element-wise
👉 Faster than lists (vectorization)
👉 Built-in functions: square, sqrt, sin, cos, tan

