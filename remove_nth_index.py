#15.WAP to remove the nth index character from a nonempty string.
#1st way
sentence = "Python Programming is fun."
str=sentence
print(str)
n = 8
print("\nstring after removing ",n,"th character: ")
str=str.replace(str[n],"")
print(str)


#2nd way
new_str = ''
n=4
for char in range(0, len(str)):
    if(char != n):
        new_str += str[char]
 
print("\nstring after removing ",n,"th character: ")
print(new_str)