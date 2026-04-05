name1=input("Enter the name of first person: ")
name2=input("Enter the name of second person: ")
combine_string=name1+name2

lower_string=combine_string.lower()
t=lower_string.count('t')
r=lower_string.count('r')
u=lower_string.count('u')
e=lower_string.count('e')
true=t+r+u+e

l=lower_string.count('l')
o=lower_string.count('o')
v=lower_string.count('v')
e=lower_string.count('e')
love=l+o+v+e

love_score=str(true)+str(love)
if love_score<"10" or love_score>"90":
    print("Your love score is "+love_score+", you go together like coke and mentos.")
elif love_score>="40" and love_score<="50":
    print("Your love score is "+love_score+", you are alright together.")
else:    
    print("Your love score is "+love_score+".")

