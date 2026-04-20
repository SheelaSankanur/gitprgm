def count_char(s,ch):
    count=0
    for c in s:
        if c==ch:
            count+=1
    return count
print(count_char("programming","m"))