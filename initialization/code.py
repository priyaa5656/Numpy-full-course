import numpy as np

# 1. Zeros Array
zero_arr = np.zeros((2, 3))
print("Zeros Array:\n", zero_arr)

# 2. Ones Array
one_arr = np.ones((1, 3))
print("\nOnes Array:\n", one_arr)

# 3. Full Array
full_arr = np.full((3, 2), 9)
print("\nFull Array:\n", full_arr)

# 4. Identity Matrix
id_arr = np.eye(3)
print("\nIdentity Matrix:\n", id_arr)

# 5. Empty Array
empty_arr = np.empty(2)
print("\nEmpty Array:\n", empty_arr)

# 6. Arange
arange_arr = np.arange(2, 10, 2)
print("\nArange Array:\n", arange_arr)

# 7. Linspace
linspace_arr = np.linspace(1, 10, 4)
print("\nLinspace Array:\n", linspace_arr)

# 8. Random Float Array
rand_arr = np.random.rand(3, 2)
print("\nRandom Float Array:\n", rand_arr)

# 9. Random Integer Array
randint_arr = np.random.randint(1, 100, (3, 3))
print("\nRandom Integer Array:\n", randint_arr)