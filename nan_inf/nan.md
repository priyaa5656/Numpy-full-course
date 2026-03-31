# Step 1: Creating an array with NaN and Inf
```python
data1 = np.array([1, 2, np.nan, 4, np.inf])
print(data1)
```
## Explanation

### np.array() 
This is a NumPy function to create an array.
An array is a data structure similar to a list but optimized for numerical and mathematical operations.
### [1, 2, np.nan, 4, np.inf]
1, 2, 4 → Normal numbers.
np.nan → "Not a Number" → represents a missing or undefined value.
np.inf → "Infinity" → represents mathematical infinity, like 1/0.
### print(data1)
Shows the array:  [ 1.  2. nan  4. inf]
Note: NaN and Inf are valid float numbers in NumPy.

✅ Example:
```python
arr = np.array([5, np.nan, np.inf])
print(arr) 
``` 
Output: [ 5. nan inf ]



# Step 2: Check for NaN values
```python
print(np.isnan(data1))
```
Explanation

## np.isnan() -->
Stands for “is NaN?”
It checks each element of the array one by one (element-wise) and returns True if the element is NaN (Not a Number), else False.
## print(np.isnan(data1))
[False False  True False False]
## Meaning:
1 → Not NaN → False
2 → Not NaN → False
NaN → Is NaN → True
4 → Not NaN → False
Inf → Not NaN → False

✅ Example:
```python
arr = np.array([np.nan, 7, 10])
print(np.isnan(arr))  
```
Output: [ True False False ]


# Step 3: Replace NaN and Inf with finite numbers
```python
print(np.nan_to_num(data1))
```
Explanation
## np.nan_to_num()
Converts NaN and Inf to regular numbers.
Default behavior:
   NaN → 0.0
   +Inf → largest possible float (1.79769313e+308)
   -Inf → smallest possible float (-1.79769313e+308)

## Output:
[1.00000000e+000 2.00000000e+000 0.00000000e+000 4.00000000e+000 1.79769313e+308]
## Breaking it down:
1 → stays 1
2 → stays 2
NaN → converted to 0
4 → stays 4
Inf → converted to 1.79769313e+308 (largest float NumPy can handle)
## Note:
1.79769313e+308 means 1.79769313 × 10^308 (very large number)


✅ Example:
```python
arr = np.array([np.nan, np.inf, -np.inf])
clean_arr = np.nan_to_num(arr)
print(clean_arr)  
```
Output: [0.00000000e+000 1.79769313e+308 -1.79769313e+308]


Detailed Definitions
| Term            | Meaning |
|-----------------|--------|
| NaN             | Not a Number → Represents Missing/invalid/undefined value |
| Inf             | Infinity → Very large number |
| np.isnan()      | Checks if value is NaN and Returns boolean array|
| np.nan_to_num() | Converts NaN/Inf to finite values |


## Key Notes

### Why we handle NaN/Inf?
Many mathematical operations (like sum, mean) fail with NaN/Inf.
Cleaning these values ensures calculations don’t break.
Custom replacement: You can replace with your own numbers:
NaN is not equal to anything, even itself:
np.nan == np.nan  → False


Example
```python
arr = np.array([1, np.nan, np.inf])
print(np.nan_to_num(arr, nan=-1, posinf=999, neginf=-999))
```
Output: [ 1 -1 999]

nan=-1 → replace NaN with -1
posinf=999 → replace +Inf with 999
neginf=-999 → replace -Inf with -999

## 💡 Summary in Simple Words:

NaN → Missing/invalid value → detect using np.isnan()
Inf → Extremely large value → handle using np.nan_to_num()
np.nan_to_num() → Converts non-finite values into safe numbers for computation