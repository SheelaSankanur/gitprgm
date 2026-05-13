def count_freq(nums):
    if len(nums)==0:
        return {}
    first=nums[0]
    rest=nums[1:]
    freq=count_freq(rest)
    freq[first]=freq.get(first, 0) + 1
    return freq
print(count_freq([1, 2, 3, 2, 1]))  # {1: 2, 2: 2, 3: 1}