#17.WAP to perform following opration on string: 
# (a) Find index of particular character (b) Perform string uppercase and lowercase 
# (c) Count the occurrence of a particular character in a string.

text = '\npython is popular programming language'
print(text)
print("\nindex of 't':",text.index('t'))
print("index of 'ing':",text.index('ing', 10))
print("index of 'is':",text.index('is', 6, -4))
print("index of 'f':",text.index('l', 7, -1))

print("\nUppercase:",text.upper())
print("Lowercase:",text.lower())

print("\nOccurrence of 'p':",text.count('p'))
print("Occurrence of 'a':",text.count('a'))
print("Occurrence of 'o':",text.count('o'))