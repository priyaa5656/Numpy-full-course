# 📊 Day 1: Introduction to NumPy

## 🧠 What is NumPy?

NumPy (Numerical Python) is the core library for scientific computing in Python.  
NumPy is the backbone of Machine Learning because all data is converted into arrays before processing.

---

## 👉 Uses of NumPy

- Fast mathematical operations ⚡  
- Working with multi-dimensional arrays (ndarray)  
- Machine Learning 🤖  
- Data Science 📊  
- Deep Learning 🧠  

---

## 💡 Key Idea

Python list = slow 🐢  
NumPy array = fast 🚀 (because it's written in C internally)

---

## 📦 Step 1: Install NumPy

```bash
pip install numpy
``` 
✔️ Run this in terminal (VS Code)
✔️ Installs NumPy in your system


📥 Step 2: Import NumPy
```python
import numpy as np
```

🔍 Step 3: Check version
```python
print(np.__version__)
``` 


📘 Array
🧠 What is an Array?
Array is a data structure that stores multiple values of the same data type in a single variable.
👉 Array is container in which Multiple values are stored.
all values are same type (int, float, etc.)

🧠 1. List making
```python
list1 = [1,2,3]
print(list1)
```
👉 list1 = Python list
👉 Output:
[1, 2, 3]  ✔️ List me commas aate hain (normal Python)


🔁 2. List → NumPy Array
```python
arr_list1 = np.array(list1)
print(arr_list1)
```
👉 np.array() = list ko NumPy array me convert karta hai
output:
[1 2 3]    NumPy array me comma nahi hota ❗



3. Type check
```python
print(type(arr_list1))
```
👉 Output:
<class 'numpy.ndarray'>  ✔️ Matlab ye NumPy array hai



4. Dimension check
```python
print(arr_list1.ndim)
```
👉 Output:
1  ✔️ Ye 1D array hai (single line)



5. 2D Array
```python
list1 = [1,2,3]
list2 = [4,5,6]
arr_list1_2 = np.array([list1, list2])
print(arr_list1_2)
```
👉 Output:
[[1 2 3]
 [4 5 6]]



6. Dimension check
```python
print(arr_list1_2.ndim)
```
👉 Output:
2 ✔️ Ye 2D array hai



7. 3D Array
```python
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
arr_list1_3 = np.array([[list1, list2, list3]])
print(arr_list1_3)
```
👉 Output:
[[[1 2 3]
  [4 5 6]
  [7 8 9]]]



8. Dimension check
```python
print(arr_list1_3.ndim)  
```
👉 Output:
3 ✔️ Ye 3D array hai  


🧠 Key Points (Important for Notes 🔥)
Array stores multiple values in one variable
All elements should be same data type
Faster than Python lists
Used in Machine Learning, Data Science