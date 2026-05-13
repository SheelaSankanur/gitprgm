def sum_odd(nums):
    if len(nums) == 0:
        return 0
    else:
        first = nums[0]
        rest = nums[1:]
        sum_rest = sum_odd(rest)
        if first % 2 == 1:
            return first + sum_rest
        else:
            return sum_rest

print("Sum of odds:", sum_odd([1, 2, 3, 4, 5]))  # 9