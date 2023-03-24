#11.WAP to find HCF of two number.

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
if num1 > num2:
 smaller = num2
else:
 smaller = num1

for i in range(1, smaller):
    if((num1 % i == 0) and (num2 % i == 0)):
        hcf = i 

print("The H.C.F. is",hcf)
