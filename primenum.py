def isPrime(n):
    if n<=1: #3
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True

n=int(input("Enter the number:"))

if isPrime(n):
    print(n,"is a prime number")
else:
    print(n,"is not prime number")