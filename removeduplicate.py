def remove_duplicates(nums):
    unique_set=set(nums)
    return list(unique_set) 
nums=[1,2,1,3,2,1]
print("without duplicates:",remove_duplicates(nums))