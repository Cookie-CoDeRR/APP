import numpy as np


nums = np.arange(1, 11)

print("Array:", nums)
print("First five:", nums[:5])
print("Even positions:", nums[1::2])
print("Sum:", nums.sum())
print("Mean:", nums.mean())
print("Maximum:", nums.max())
print("Minimum:", nums.min())

nums += 5

print("After adding 5 to every number:", nums)