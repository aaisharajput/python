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
