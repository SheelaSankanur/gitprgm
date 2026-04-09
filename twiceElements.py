def twice_elements(nums):
    freq={}
    for i in nums:
        freq[i]=freq.get(i,0)+1

    for count in freq.values():
        if count==2:
            return True
    return False
nums=[1,2,3,4,1]
print(twice_elements(nums)) 
