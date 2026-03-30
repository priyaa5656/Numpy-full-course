## 📘 Array Comparison 
👉 Array comparison means checking elements of one array with another array.
### 👉 this checks --> 
     Which elements are equal?
     Which elements are different?

### 👉 2 types of comparison:
- Element-wise comparison
- Full array comparison

## 🔹 Step 1: Creating Arrays
```python
a = np.array([1, 5, 3])
b = np.array([4, 5, 6])
```
👉 Arrays:
a → [1 5 3]  
b → [4 5 6]

## 🔹 1. Element-wise Comparison (a == b)
👉 a == b har element ko same index pe compare karta hai

```python 
print(a == b)
```

🧠 Working (step-by-step)
| a | b | Comparison | Result |
|---|---|------------|--------|
| 1 | 4 | 1 == 4     |  False |
| 5 | 5 | 5 == 5     | True   |
| 3 | 6 | 3 == 6     | False  |

👉 Output: [False  True  False]
✔️ The check is performed at the same position.
✔️ The result is returned as a boolean (True/False).

## 🔹 2. Full Array Comparison (np.array_equal())
👉 np.array_equal() check karta hai ki dono arrays completely same hain ya nahi

```python
print(np.array_equal(a, b))
```
### 🧠 Working 👉 Condition:
Size should be the same.
All elements should be the same.

👉 Check:
a = [1 5 3]
b = [4 5 6]

👉 Is this equal?  
❌ no

👉 Output:  False

## 🔥 Important Difference   
| Method |                        Meaning |
|--------|--------------------------------|
| a == b |        element-wise comparison |
| np.array_equal() |full array comparison |


## 🎯 One-line Summary (Notes 🔥)   
👉 == → compare element by element   
👉 array_equal → compare full array   
