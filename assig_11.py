import numpy as np
import pandas as pd


nums = pd.Series(np.random.randint(1, 101, 10))

print("Series:")
print(nums)
print("First number:", nums.iloc[0])
print("Numbers from index 2 to 5:")
print(nums.iloc[2:6])
print("Numbers greater than 50:")
print(nums[nums > 50])
print("Mean:", nums.mean())
print("Median:", nums.median())
print("Minimum:", nums.min())
print("Maximum:", nums.max())