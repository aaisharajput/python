#21.WAP to illustrate difference between POP, Del, and Clear
l = [0, 1, 2, 3, 4, 3, 5, 0, 6, 7, 7, 8, 9, 5, 6, 10, 50, 20, 90, 80, 55, 34, 64, 101, 348, 5, 64, 123, 7]
print("\nList(l): ",l)

#pop
print("\nl.pop(0): ",l.pop(0))
print(l)
print("\nl.pop(3): ",l.pop(3))
print(l)
print("\nl.pop(-2): ",l.pop(-2))
print(l)
print("\nl.pop(): ",l.pop())
print(l)

#del
del l[0]
print("\ndel l[0]: ",l)
del l[3]
print("\ndel l[3]: ",l)
del l[-1]
print("\ndel l[-1]: ",l)
del l[-2]
print("\ndel l[-2]: ",l)
del l[2:5]
print("\ndel l[2:5]: ",l)
del l[:3]
print("\ndel l[:3]: ",l)
del l[-2:]
print("\ndel l[-2:]: ",l)
#specify step as [start:stop:step].
del l[::2]
print("\ndel l[::2]: ",l)
del l[:] #delete entire list
print("\ndel l[:]: ",l)

l = [0, 1, 2, 3, 4, 3, 5, 0, 6, 7, 7, 8, 9, 5, 6, 10, 50, 20, 90, 80, 55, 34, 64, 101, 348, 5, 64, 123, 7]
print("\nList(l): ",l)

#clear
l.clear()
print("l.clear(): ",l)