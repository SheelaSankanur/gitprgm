def all_subarray_sums_of_size_k(arr, k):
    if len(arr)<k:
        return []
    window_sum=sum(arr[:k])
    sums=[window_sum]

    for i in range(k,len(arr)):
        window_sum=window_sum-arr[i-k]+arr[i]
        sums.append(window_sum)
    return sums
arr=[1,2,3,4,5]
k=2
print("All sums of size",k,":", all_subarray_sums_of_size_k(arr,k))
