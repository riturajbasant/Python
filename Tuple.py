#tuple
'''
it is kind of standard datatype
it is imutable
we can not change any element of tuple
Tuple is created under paranthesis
it is collection of different datatypes
element of tuple is seperated by comma.
'''

tup=(43,3,35,54,5466,54,7688,'fdud',9584.39345)
tup1=(898,97878)
print(tup)
print(type(tup))
#concatenation
print(tup+tup1)
print(tup1*2)
for i in tup:
	print(i)
print(tup[-1])
print(tup[:])
print(tup.count(54))
print(len(tup))
del(tup)
#print(tup)
tup2=([43,343,343,343],(938,34,34,3),433)
print(tup2)

tup2[0].remove(43)
print(tup2)

#convert tuple to list

list3=list(tup2)
print(list3)
list3[0].remove(343)
print(list3)

tup3=tuple(list3)
print(tup3)

a = (34,45,56,123)
print(a.index(45))