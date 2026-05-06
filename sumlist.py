def sum_list(nums):
    if len(nums)==0:
        return 0
    else:
        return nums[0] + sum_list(nums[1:])
    
numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print("Sum of the list:", result)
