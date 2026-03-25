#employee bonus system
employee=input("enter your name:")
performance_rate=int(input("you have performance rating at least 8%"))
experience=int(input("you have experience at least 5 years"))
if experience>=5:
    if performance_rate>=8:
        print("you got 20% bonus")
    else :
        print("you got 10% bonus")
else:
    print("no bonus")