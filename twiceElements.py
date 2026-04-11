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



def remove_duplicates_keep_order(nums):
    seen = set()
    result = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
nums = [1, 2, 1, 3, 2, 1]
print("Order preserved:", remove_duplicates_keep_order(nums))


def common_elements(nums1,nums2):
    set1=set(nums1)
    set2=set(nums2)
    common=set1 & set2
    return list(common)
nums1=[1,2,2,3]
nums2=[2,3,4]
print(common_elements(nums1,nums2))
