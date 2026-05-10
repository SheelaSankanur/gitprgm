def analyze_list(nums):
    evens = []
    odds = []
    total = 0

    for x in nums:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)
        total += x

    return {
        "evens": evens,
        "odds": odds,
        "sum": total
    }

nums = [1, 2, 3, 4, 5, 6]
result = analyze_list(nums)
print(result)