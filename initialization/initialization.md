📘 Array Initialization Methods
👉 Array initialization methods are used to create NumPy arrays with predefined values, patterns, or ranges.
OR 👉 We create arrays using various methods (0s, 1s, random, range, etc.).

🔹 1. Zeros Array
👉 np.zeros() creates an array of a given shape where all elements are 0. or np.zeros() is a function that creates a NumPy array filled with zeros.
```python
zero_arr = np.zeros((2,3))
print(zero_arr)
```
🧠 Word-by-word:
np.zeros → creates an array of a given shape where all elements are 0.
(2,3) → shape (2 rows, 3 columns)

👉 Output:

[[0. 0. 0.]
 [0. 0. 0.]]    ✔️ Har element = 0   ✔️ Decimal (0.) → float type

🔹 2. Ones Array
👉 np.ones() is a function that creates a NumPy array filled with ones.
```python
one_arr = np.ones((1,3))
print(one_arr)
```
🧠
np.ones → all elements = 1
(1,3) → shape - 1 row, 3 columns

👉 Output:

[[1. 1. 1.]]


🔹 3. Full Array
👉 np.full() is a function that creates a NumPy array filled with a specified value or given value. 
```python
full_arr = np.full((3,2), 9)
print(full_arr)
```
🧠:
np.full → a function that creates a NumPy array filled with a specified value.
(3,2) → 3 rows, 2 columns
9 → all  element = 9

👉 Correct Output:

[[9 9]
 [9 9]
 [9 9]]


🔹 4. Identity Matrix
👉 👉 In an identity matrix, the diagonal elements are equal to 1, and all other elements are equal to 0.
```python
id_arr = np.eye(3)
print(id_arr)
```
👉 Output:

[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]] ✔️ Diagonal = 1  ✔️ Baaki = 0


🔹 5. Empty Array
👉 np.empty() allocates memory for an array but does not initialize its values. OR 👉 np.empty() → creates an array without initializing values (contains garbage values)
```python
print(np.empty(2))
```
(2) → 2 elements

👉 Output:
[1.20e-311 0.00e+000] ✔️ Random values (garbage values) ❗ Use carefully


🔹 6. Arange (Range Array)
👉  np.arange() is a function that creates a NumPy array with evenly spaced values within a given range.
```python
print(np.arange(2,10,2))
```
🧠:
2 → start
10 → end (exclude hota hai)
2 → step

👉 Output:
[2 4 6 8] ✔️ 2 se start  ✔️ 2-2 ka gap


🔹 7. Linspace
👉 np.linspace() is a function that generates a fixed number of equally spaced values between a start and an end point.
```python
print(np.linspace(1,10,4))
```
🧠 Samajh:
1 → start
10 → end
4 → total values

👉 Output:
[1. 4. 7. 10.] ✔️ Equal spacing  ✔️ Total 4 values


🔹 8. Random Float 
👉 np.random.rand() is a function that creates an array of random floating-point numbers between 0 and 1.
```python
r_arr = np.random.rand(3,2)
print(r_arr)
```
🧠 Samajh:
np.random.rand → random float values (0 to 1)
(3,2) → shape

👉 Output (example):
[[0.45 0.78]
 [0.12 0.67]
 [0.89 0.23]]    ❗ all times different value

🔹 9. Random Integer Array
👉 np.random.randint() is a function that generates random integers within a specified range.
OR   👉 It creates an array of random integers between a given minimum and maximum value.
```python
rint_arr = np.random.randint(1,100,(3,3))
print(rint_arr)
```
🧠 Samajh:
1 → minimum
100 → maximum (exclude)
(3,3) → shape

👉 Output (example):

[[60 13 62]
 [ 3 36 14]
 [96 78 10]]

✔️ Random integers
