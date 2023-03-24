#9.WAP to generate first 50 prime number series. Also check whether given any 2 numbers are coprime or not.
first50=0
i=2
print("First 50 Prime number series:")
while first50<=50:
    n=i
    count=0
    for j in range(2,n//2+1):
        if n%j==0:
            count+=1
    if count==0:
        print(i)
        first50+=1
    i+=1
    
num1=int(input("Enter 1st no.: "))
num2=int(input("Enter 2nd no.: "))
if num1<num2:
    small=num1
else:
    small=num2

i=2
while i<=small:
    if num1%i==0 and num2%i==0:
        break
    i+=1
if i<=small:
    print("Given two no. is not a co-prime no.")
else:
    print("Given two no. is a co-prime no.")