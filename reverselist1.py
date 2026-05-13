def reverse_list(nums):
    if len(nums) <= 1:               # base: 0 or 1 element
        return nums
    else:
        first = nums[0]
        rest = nums[1:]
        reversed_rest = reverse_list(rest)
        return reversed_rest + [first]

print(reverse_list([1, 2, 3, 4]))  # [4, 3, 2, 1]
