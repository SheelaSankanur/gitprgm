import random
names=input("enter everybody's name, separated by a comma: ")
name_list=names.split(",")
length=len(name_list)
random_choice=random.randint(0, length-1)
print(f"{name_list[random_choice]} is going to buy the meal today!")
