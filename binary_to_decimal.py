#10.WAP to convert a binary number into decimal number and then calculate the sum of digits of decimal number.
n=int(input("Enter binary number: "))
decimal = 0
power = 1
while n>0:
    rem = n%10
    n = n//10
    decimal += rem*power
    power = power*2
print("Decimal value: ",decimal)
        
n=decimal
sum = 0
while (n != 0):
    sum = sum + (n % 10)
    n = n//10
print("sum of digits: ",sum)