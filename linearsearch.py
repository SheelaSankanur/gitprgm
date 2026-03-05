def linearsearch(arr,sz,tar):
    for i in range(sz):
        if arr[i]==tar:
            return i
        
    return -1

arr=[4,2,5,7,8,9]
sz=len(arr)
tar=8
print(linearsearch(arr,sz,tar))