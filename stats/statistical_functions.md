# 📘 Statistical Functions in NumPy
👉 Statistical functions are used to calculate mathematical properties of an array such as sum, mean, median, standard deviation, minimum, and maximum.
👉 These are used for array data analysis.

## 🔹 Step 1: Creating an Array
```python
a = np.array([[1,2,3], [4,5,6]])
print(a)
```
👉 Output:
[[1 2 3]
 [4 5 6]]

 🧠:  2 rows, 3 columns
        Elements: 1,2,3,4,5,6


## 🔹 1. Sum
👉 np.sum() returns the total sum of all elements in the array.  
```python
print(np.sum(a))
```
🧠 Working:  1 + 2 + 3 + 4 + 5 + 6 = 21
👉 Output:  21

## 🔹 2. Mean (Average)
👉 np.mean() returns the average of all elements.
```python
print(np.mean(a))
```
#### 🧠 Formula:
#### Mean = Sum / Total elements

🧠 Working:
Sum = 21
Elements = 6
Mean = 21 / 6 = 3.5

👉 Output:  3.5


## 🔹 3. Median
👉 np.median() returns the middle value of sorted data.
```python
print(np.median(a))
```
🧠 Working:
Data = [1,2,3,4,5,6]
Middle values = 3 and 4
Median = (3 + 4) / 2 = 3.5

👉 Output:  3.5


## 🔹 4. Standard Deviation (std)
👉 np.std() measures how much the values are spread out from the mean.
```python
print(np.std(a))
```
👉 Output: 1.7078 (approx)

✔️ Low std → values are closed
✔️ High std → values are far


## 🔹 5. Minimum
👉 np.min() returns the smallest value in the array.
```python
print(np.min(a))
```
👉 Output: 1


## 🔹 6. Maximum
👉 np.max() returns the largest value in the array.
```python
print(np.max(a))
```
👉 Output:6

### 🎯 One-line Summary (Notes 🔥)
👉 sum → total
👉 mean → average
👉 median → middle value
👉 std → spread of data
👉 min → smallest
👉 max → largest