#8.WAP to generate a random number and then calculate its sum of digits.
import random
n=random.randint(0,100)
print("Number: ",n)

sum = 0
while (n != 0):
    sum = sum + (n % 10)
    n = n//10
print("sum of digits: ",sum)