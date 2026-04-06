def move_zeros(lst):
    res=[]
    zeros=0
    for num in lst:
        if num==0:
            zeros+=1
        else:
            res.append(num)
    for _ in range(zeros):
        res.append(0)
    return res
print(move_zeros([0, 1, 0, 3, 12]))