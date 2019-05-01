#isdisjoint is used to check if two sets have anyvalue in common, if nothing is common then it prints true.
'''
set1={32,56,12,23}
set2={231,543,12}
print(set1.isdisjoint(set2))
'''

#issuperset: it checks that set2 values are there in set1, if present then set1 is supperset of set2
'''
set1 = {32,45,54,67,98}
set2= {54,98,77}

print(set1.issuperset(set2))
'''
'''
#issubset : Here set2 is subset of set1 as all the values of set2 should be there in set1.
set1={32,53,65,77,343}
set2={12,32,53}
print(set2.issubset(set1))
#clear : is used to clear the values of sets.

#copy : is used to copy one set into another

set1={34,56,12,76,98}
print(id(set1))
set1=set1.copy()
print(id(set1))


#Sort : it will sort the data into list and it can't sort in set
set1={34,54,67,2,51,21}
print(sorted(set1))

'''
#frozen set is a mutable standard datatype, hence we can't change the value of frozen set


set1=frozenset([43,23,545,64,43])
print(set1)
