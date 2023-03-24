#12.WAP to display Fibonacci series.

num1=0
num2=1

print("Fibonacci Series: ")
for i in range(1,20):
    print(num1)
    fab=num1+num2
    num1=num2
    num2=fab

