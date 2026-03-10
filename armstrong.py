def isArmstrong (n):
    copyN=n
    sumofCubes=0
    while n!=0 :
        digit=n%10
        sumofCubes=(digit*digit*digit)
        n=n/10
    
    return sumofCubes==copyN
 

n=111
if(isArmstrong(n)):
    print("is an armstrong number")
else:
    print(n,"is not an armstrong number")