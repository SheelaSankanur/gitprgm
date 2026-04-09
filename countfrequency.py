def count_freq(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
nums=[1,2,1,3,2,1]
print(count_freq(nums))
    