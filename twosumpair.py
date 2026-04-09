def two_sum_pair(nums,target):
    left=0
    right=len(nums)-1

    while left<right:
        curr_sum=nums[left]+nums[right]

        if curr_sum==target:
            return [nums[left],nums[right]]   #numbers
            #return [left,right]  #indices 
        elif curr_sum<target:
            left+=1
        else:
            right-=1
    return[]
nums=[1,2,4,7,11,15]
print("pair for 9:",two_sum_pair(nums,9))
print("pair for 50:",two_sum_pair(nums,50))
        