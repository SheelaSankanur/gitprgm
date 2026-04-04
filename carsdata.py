import pandas as pd

my_dataset={
    'Car':['BMW','AUDI','MERCEDES'],
    'Price':[50000,45000,55000], 
}
df=pd.DataFrame(my_dataset)
print(df.to_string())  


# import pandas as pd
# a=[1,2,3,4,5]
# myvar=pd.Series(a,index=['a','b','c','d','e'])
# print(myvar) 