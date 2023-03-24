#19.WAP to remove the first occurrence of a specified element from a list.

list = [10, 20, 30, 40, 30, 40, 30]

print("\nList element: ",list)
n=int(input("Enter number to remove: "))

list.remove(n)
print("List element after removing ",n,": ",list)
