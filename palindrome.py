def palindrome(n):
    original=n
    rev=0

    while n!=0:
        digit=n%10 
        rev=rev*10+digit
        n=n//10 
    return original == rev
n=int(input("enter number:"))
if palindrome(n):
    print(n,"this is palindrome")
else:
    print(n,"this is not palingrome") 
