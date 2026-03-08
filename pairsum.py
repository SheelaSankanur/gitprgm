def pairsum(nums,tar):
    n=len(nums)
    ans=[]
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==tar:
                ans.append(i)
                ans.append(j)
                return ans
    return ans 
nums=[2,7,14,1,5,0]
tar=8
ans=pairsum(nums,tar)
print(ans[0] ,",",ans[1])