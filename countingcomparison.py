def linear_search_with_count(nums,tar):
    count=0
    for i in range(len(nums)):
        count+=1
        if nums[i]==tar:
            return i,count
    return -1,count

nums=[1,2,3,4,5,6,7,8,9,10]
idx,steps=linear_search_with_count(nums,7)
print(f"Element found at index: {idx}, Steps taken: {steps}")
