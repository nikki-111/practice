n=int(input("enter  number: "))
if n>1:
    for i in range(2,(n//2)+1):
        if n%i==0:
            print("number is not prime number")
        
        else:
            print("number is prime number")
        break
else:
    print("number is not prime number")
        