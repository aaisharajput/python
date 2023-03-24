#13.WAP to check whether a number is (a) Palindrome (b) Armstrong.

rev=0
num=int(input("Enter a number: "))
original=num
sum=0
while num>0:
    rem=num%10
    sum=sum+rem**3
    rev=(rev*10)+rem
    num=num//10

if original==rev:
    print(original," is a palindrome number.\n")
else:
    print(original," is not a palindrome number.\n")
    
if original==sum:
    print(original," is a Armstrong number.")
else: 
    print(original," is a not Armstrong number.")