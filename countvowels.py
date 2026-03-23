#count vowels
s="python programming"
count=0
for i in s:
    if i.lower() in "aeiou":
        count+=1
print(count)