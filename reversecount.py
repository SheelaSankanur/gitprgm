def filter_reverse_count(nums):
    evens = []                        # filter evens
    for x in nums:
        if x % 2 == 0:
            evens.append(x)

    reversed_evens = evens[::-1]      # reverse
    return reversed_evens, len(evens)

nums = [1, 2, 3, 4, 5, 6]
rev, cnt = filter_reverse_count(nums)
print("Reversed evens:", rev)   # [6, 4, 2]
print("Count:", cnt)            # 3