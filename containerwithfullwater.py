def maxWater(arr):
    n=len(arr)
    res=0
    for i in range(n):
        for j in range(i+1,n):
            amount=min(arr[i],arr[j])*(j-i)
            res=max(amount,res)
    return res
if __name__=="__main__":
    arr=[2, 1, 8, 6, 4, 6, 5, 5]
    res=maxWater(arr)
    print(res)  