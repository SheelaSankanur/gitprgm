def twosum(arr,tar):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==tar:
                return True
    return False
if __name__=="__main__":
    arr=[0,-1,2,-3,1]
    tar=-2
    if twosum(arr,tar):
        print("True")
    else:
        print("False")
