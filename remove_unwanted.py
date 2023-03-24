#16.WAP to remove unwanted characters such as #, $, %, &. *, (, ), ^, etc. from a given string.

unwanted_chars = ['#','$','%','&','(',')','^',';', ':', '!', '*','-','@','_']

test_string = "Py@th;on Prog%ram-m*ing i$s F(u)n"

print("\nOriginal String : " + test_string)

for i in unwanted_chars:
    test_string = test_string.replace(i, '')
 
print("\nafter removing unwanted character: " + str(test_string))