def count_freq(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

def find_duplicates(nums):
    freq=count_freq(nums)
    duplicates=[]
    for i,count in freq.items():
        if count>1:
            duplicates.append(i)
    return duplicates
nums=[1,2,1,3,2,1]
print("Duplicates:",find_duplicates(nums))
