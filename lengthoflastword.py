def lengthOflastword(s):
    words=s.strip().split()
    return len(words[-1])
s="hello world"
print(lengthOflastword(s))
