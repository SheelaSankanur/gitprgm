def myPow(x,n):
    bin=n
    ans=1
    if (n<0):
        bin=(-1)*bin
        x=1/x
    while bin>0:
        if bin%2==1:
            ans*=x
        x*=x
        bin//=2
    return ans
x=int(input("enter the base:"))
n=int(input("enter exponent:"))
print("power is:",myPow(x,n))
