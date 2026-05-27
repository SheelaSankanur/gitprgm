def spiralmatrix(mat):
    m=len(mat)
    n=len(mat[0])

    res=[]
    vis=[[False]*n for _ in range(m)]

    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    r,c=0,0
    idx=0
    for _ in range(m*n):
        res.append(mat[r][c])
        vis[r][c]=True
        nr,nc=r+dr[idx],c+dc[idx]
        if 0<=nr<m and 0<=nc<n and not vis[nr][nc]:
            r,c=nr,nc
        else:
            idx=(idx+1)%4
            r+=dr[idx]
            c+=dc[idx]
    return res
if __name__=="__main__":
    mat=[[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    res=spiralmatrix(mat)
    print("".join(map(str,res)))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
