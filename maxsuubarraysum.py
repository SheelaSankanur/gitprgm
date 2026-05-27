def maxsubarraysum(arr):
    res=arr[0]
    for i in range(len(arr)):
        curr_sum=0
        for j in range(i,len(arr)):
            curr_sum+=arr[j]
            res=max(res,curr_sum)
    return res
if __name__=="__main__":
    arr=[-2,1,-3,4,-1,2,1,-5,4]
    print("max subarray sum:",maxsubarraysum(arr))  # Output: 6