# ==============================
# 📘 BROADCASTING + VECTORIZATION DEMO
# ==============================

import numpy as np

print("🔥 NumPy Broadcasting + Vectorization Demo 🔥\n")

# ======================================
# 1. BROADCASTING (BASIC)
# ======================================

print("=== Example 1: 1D + single value ===")

a = np.array([1, 2, 3, 4])
b = np.array([5])

print("a:", a)
print("b:", b)

result = a + b
print("Result:", result)
print()


# ======================================
# 2. 2D + 1D BROADCASTING
# ======================================

print("=== Example 2: 2D + 1D ===")

c = np.array([[1, 2, 3],
              [4, 5, 6]])

d = np.array([10, 20, 30])

print("c:\n", c)
print("d:", d)

result = c + d
print("Result:\n", result)
print()


# ======================================
# 3. ERROR CASE (IMPORTANT)
# ======================================

print("=== Example 3: ERROR CASE ===")

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20])  # ❌ mismatch

print("Trying invalid operation...")

try:
    print(a + b)
except ValueError as e:
    print("❌ ERROR:", e)

print()


# ======================================
# 4. COLUMN BROADCASTING
# ======================================

print("=== Example 4: Column Broadcasting ===")

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[10],
              [20]])

print("a:\n", a)
print("b:\n", b)

result = a + b
print("Result:\n", result)
print()


# ======================================
# 5. VECTOR + MATRIX BROADCASTING
# ======================================

print("=== Example 5: 1D + Column Vector ===")

a = np.array([1, 2, 3])
b = np.array([[10],
              [20]])

print("a:", a)
print("b:\n", b)

result = a + b
print("Result:\n", result)
print()


# ======================================
# 6. VECTORIZATION (NO LOOP)
# ======================================

print("=== Vectorization Examples ===")

a = np.array([1, 2, 3])

print("Original:", a)

print("Multiply by 2:", a * 2)
print("Square:", a ** 2)
print("Add:", a + np.array([4, 5, 6]))
print("Divide:", a / 2)

print()


# ======================================
# 7. PRACTICE CHECK
# ======================================

print("=== Practice Check ===")

print("[1,2,3] + 5 =", np.array([1,2,3]) + 5)
print("[2,4,6] * 3 =", np.array([2,4,6]) * 3)
print("[1,2,3] + [3,2,1] =", np.array([1,2,3]) + np.array([3,2,1]))
print("[5,10,15] / 5 =", np.array([5,10,15]) / 5)
print("[2,3,4] ** 2 =", np.array([2,3,4]) ** 2)

print()


# ======================================
# 🎯 FINAL SUMMARY
# ======================================

print("=== SUMMARY ===")
print("✔ Broadcasting = shape match karke expand karta hai")
print("✔ Vectorization = loop hata ke fast calculation karta hai")
print("✔ Together = FAST + FLEXIBLE computation 🚀")