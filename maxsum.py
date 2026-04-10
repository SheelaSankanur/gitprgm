#sliding window :Instead of looping again and again over the same elements

def max_sum_subarray(arr,k):
    if len(arr)<k:
        return 0
    #step 1:compute sum of first window
    window_sum=sum(arr[:k])
    max_sum=window_sum

    #step 2:Slide the window from start=1 to end=len(arr)-1
    for i in range(k,len(arr)):
        window_sum=window_sum-arr[i-k]+arr[i]
        max_sum=max(max_sum,window_sum)
    return max_sum

arr=[2,1,5,1,3,2]
k=3
print("Max sum of size",k,":",max_sum_subarray(arr,k)) 
