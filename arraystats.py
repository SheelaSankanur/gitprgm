def array_stats(nums):
    total=0
    evens=[]
    odds=[]
    for x in nums:
        total +=x
        if x%2==0:
            evens.append(x) 
        else:
            odds.append(x)
    return {"sum": total,
        "evens": evens,
        "odds": odds,
        "count": len(nums)
    }
print(array_stats([1, 2, 3, 4, 5]))  # {"sum": 15, "evens": [2, 4], "odds": [1, 3, 5], "count": 5}