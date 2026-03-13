def removeElement(nums,val):
    k=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[k]=nums[i]
            k+=1
    return k

nums=[0,1,2,2,3,0,4,2]
val=2
k=removeElement(nums,val)
print("k=",k)
print("updated array=",nums[:k])