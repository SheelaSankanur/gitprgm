#remove duplicates from list using set and convert back to tuple 
list=[1,2,2,3,4,4,5,5]
remove_set=set(list)
print(type(remove_set))
result_tuple=tuple(remove_set)
print(list)
print("tuple without dupicates",result_tuple)