def longestuniquesubstr(s):
    n=len(s)
    res=0
    for i in range(n):
        visited=[False]*26
        for j in range(i,n):
            if visited[ord(s[j])-ord('a')]==True:
                break
            else:
                res=max(res,j-i+1)
                visited[ord(s[j])-ord('a')]=True
    return res
if __name__=="__main__":
    s="abcabcbb"
    res=longestuniquesubstr(s)
    print(res)  # Output: 3 (the longest substring without repeating characters is "abc")