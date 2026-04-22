def sort_descending(nums):
    return sorted(nums, reverse=True)
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_descending(numbers)
print("Original list:", numbers)
print("Sorted list (descending):", sorted_numbers)