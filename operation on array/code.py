import numpy as np

# -----------------------------
# Speed Comparison (Concept)
# -----------------------------

# Python List (slow)
numbers_list = list(range(1, 1000001))
result_list = [x + 5 for x in numbers_list]

# NumPy Array (fast)
numbers_np = np.arange(1, 1000001)
result_np = numbers_np + 5


# -----------------------------
# Basic Mathematical Operations
# -----------------------------
a = np.array([10, 20, 40, -30])
print("Array:", a)

print("Add 10:", a + 10)
print("Subtract 30:", a - 30)
print("Multiply by 2:", a * 2)
print("Divide by 10:", a / 10)


# -----------------------------
# Advanced Functions
# -----------------------------
b = np.array([1, 4, 9])
print("\nArray b:", b)

print("Square:", np.square(b))
print("Square Root:", np.sqrt(b))


# -----------------------------
# Trigonometric Functions
# -----------------------------
print("\nSin:", np.sin(b))
print("Cos:", np.cos(b))
print("Tan:", np.tan(b))