import numpy as np

# 1. Array Creation
arr = np.array([10, 20, 30, 40, 50, 60])
print("Original Array:")
print(arr)

# 2. Indexing
print("\nIndexing:")
print("First element:", arr[0])
print("Third element:", arr[2])
print("Last element:", arr[-1])

# 3. Slicing
print("\nSlicing:")
print("Elements from index 1 to 4:", arr[1:5])
print("First three elements:", arr[:3])
print("Last three elements:", arr[-3:])

# 4. Reshaping
arr2 = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr2.reshape(2, 3)

print("\nReshaped Array (2 x 3):")
print(reshaped_arr)

# 5. Mathematical Operations
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("\nMathematical Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Square and Square Root
print("Square of a:", a ** 2)
print("Square root of a:", np.sqrt(a))