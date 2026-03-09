set1={1,2,3,4,5}
set2={3,4,6,7}
intersection_set=set()
print(type(intersection_set)) 

for i in set1:
   if i in set2:
        intersection_set.add(i)
print("set 1:",set1)
print("set 2:",set2)
print("intersection set:",intersection_set)
