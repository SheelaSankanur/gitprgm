def fibbonacci(n):
    if n<=1:
        return 1
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)

n=int(input("enter the number:"))
print(fibbonacci(n))
