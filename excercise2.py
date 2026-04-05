size=input("what is the size of the pizza you want? S, M, or L:")
bill=0
if size=="S" or size=="s":
    bill+=100
    print("Small pizza price is 100rs.")
elif size=="M" or size=="m":
    bill+=200
    print("Medium pizza price is 200rs.")
elif size=="L" or size=="l":
    bill+=250
    print("Large pizza price is 250rs.")
add_pepperoni=input("Do you want pepperoni? Y or N:")
if add_pepperoni=="Y" or add_pepperoni=="y":
    if size=="S" or size=="s":
        bill+=20
        print("Pepperoni for small pizza is 20rs.")
    else:
        bill+=30
        print("Pepperoni for medium or large pizza is 30rs.")
extra_cheese=input("Do you want extra cheese? Y or N:")
if extra_cheese=="Y" or extra_cheese=="y":
    bill+=20
    print("Extra cheese is 20rs.")
print(f"Your final bill is {bill} rs.")