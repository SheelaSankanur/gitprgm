def sum_even(nums):
    if len(nums) == 0:
        return 0
    else:
        first = nums[0]
        rest = nums[1:] 
        sum_rest = sum_even(rest)
        if first % 2 == 0:
            return first + sum_rest 
        else:
            return sum_rest
nums = [1, 2, 3, 4, 5, 6]
result = sum_even(nums)
print(f"Sum of even numbers in {nums} is: {result}")