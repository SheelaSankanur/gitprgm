nums = [3, 1, 4, 1, 5]

# 1. New sorted list
sorted_asc = sorted(nums)
print("Original:", nums)        # [3, 1, 4, 1, 5]
print("Sorted :", sorted_asc)   # [1, 1, 3, 4, 5]

# 2. In‑place sort
nums.sort()
print("After nums.sort():", nums)  # [1, 1, 3, 4, 5]