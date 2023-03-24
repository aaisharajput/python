#20.WAP to illustrate different method in (a) List (b) Tuple (c) Dictionary.
#list
f1=["Italy", "Argentina","Germany", "Brazil","France","Brazil","Italy","Spain","Germany", "France"]
print("\nList:",f1)
print("\nType of list:",type(f1))
print("\nCount 'France':",f1.count('France'))
f1.append("India")
print("\nAppend 'India':",f1)
f1.append(26)
print("\nAppend 26:",f1)
f1.insert(5,"Korea")
print("\nInsert 'Korea' at 5th index:",f1)
print("\nLength of list:",len(f1))
print("\nIndex of 'Brazil':",f1.index('Brazil'))
f1.remove('Italy')
print("\nRemove 'Italy':",f1)
print("\nPop value:",f1.pop())
print("\nList:",f1)
print("\nPop 3rd index value:",f1.pop(3))
print("\nList:",f1)
a=f1.index("France")
f1[a]="McLaren"
print("\nReplace 'France' with 'McLaren':",f1)
f1.sort(reverse=True)
print("\nSort in decending order:",f1)
f1.sort(reverse=False)
print("\nSort in ascending order:",f1)

#Tuple
tr=('He','Ne','Ar','Xe','Kr','Xe','Rn','Xe')
print("\n\nTuple:",tr)
print("\nType of list:",type(tr))
print("\nLength of Tuple:",len(tr))
print("\nIndex of 'Kr':",tr.index('Kr'))
print("\nCount 'Xe':",tr.count('Xe'))
del tr
print("\ndel tr: Delete Tuple")

#Dictionary
d1={ 'Front Camera' : '16 MP',
      'Battery' : '3300mAh',
      'Processor':	'Qualcomm Snapdragon 845',
      'RAM':	'6 GB',
      'Fast Charge'	:True
    }
print("\n\nDictionary: ",d1)
print("\nLength of Dictionary:",len(d1))
print("\nKeys of Dictionary:",d1.keys())
print("\nValue for the first key(using key): ",d1['Front Camera'])
print("\nValue for the second key(using key): ",d1['Battery'])
print("\nValue for the fourth key(using get() method): ",d1.get('RAM'))
print("\nValue of Dictionary(using values() method): ",d1.values())
print("\nRetrieve all the items stored in the 'my_dict' dictionary as a collection of tuples: \n",d1.items())
print("\nAdd 'Memory' and '128 GB' as keys and values respectively to the dictionary")
d1['Memory']='128 GB'
print("\nDictionary: ",d1)
print("\nRemove the item 'Battery' : '3300 mAh' from the dictionary")
d1.pop('Battery')
print("\nDictionary: ",d1)
print("\nRemove the last item from the dictionary")
d1.popitem()
print("\nDictionary: ",d1)
