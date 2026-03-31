# 📘 Save & Load Arrays in NumPy
## 🔹 np.save()
np.save() is a function used to save a NumPy array into a file in binary (.npy) format.

## 🔹 Code
```python
arr = np.array([1,0,0,8])
print(arr)
np.save('my_array.npy', arr)
```
### 🧠 Word-by-word Explanation
🔹 arr = np.array([1,0,0,8])
👉 np.array() → creating array 
👉 [1,0,0,8] → values
👉 Result:   [1 0 0 8]
🔹 np.save('my_array.npy', arr)
👉 np.save() → a function used to save array into file 
🔹 ('my_array.npy', arr)
👉 .npy →special binary format of numpy (fast + compact 💻)
👉 arr →  save this array
👉my_array.npy  → file name 
👉.npy is a binary file format used by NumPy to store array data efficiently.
✔️ Result:
👉 file is created → my_array.npy

## 🔹 np.load()
np.load() is a function used to load a NumPy array from a saved .npy file.
```python
loaded_arr = np.load('my_array.npy')
print(loaded_arr)
```

### 🧠 Word-by-word Explanation
🔹 loaded_arr = np.load('my_array.npy')
👉 np.load() → Loads the saved file.
👉 'my_array.npy' → file name
👉 loaded_arr → The variable that will receive the data.
🔹 print(loaded_arr)
👉 Output: [1 0 0 8]

✔️ getback Same data  🔥

🎯 One-line Summary
👉 np.save() → array save
👉 np.load() → array load
  
  
🔹 Save & Load (Concept)
Saving and loading arrays means storing data to disk and retrieving it later without losing information.

🎯 One-line Summary (Notes 🔥)

👉 np.save() →  save the array
👉 np.load() →  load the array  
👉 .npy →  fast file format of NumPy