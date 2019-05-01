#Dictionary: is a mutable datatype it doesn't use index to access element of disctionary. Here we use key instead of index. We declare dictionary under curlybrackets. Each element of dictionary has one key and one value. Key and value is seperated by : and element of dictionary seperated by comma. Key should be unique which is in either string, float, int. Values will be anything like string, int, float, list, tuple, set, function, dictionary.
#to create blank set and disctionary

'''a = set()
b = {}
print(type(a))
print(type(b))'''

a= {'A':32,'B':355}
print(a)
print(type(a))


#access of disctionary

print(a['A'])

#Update manually

a['C']=4556
print (a)

a['A']=5456
print(a)

print(a.keys())
print(a.values())

b={23:54546, 34:94358}
a.update(b)
print(a)

#iteration to generate keys and values
for i in a:
	print(i,":",a[i])
	
print(len(a))
r='1234'
print({}.fromkeys(b))

#to input somevalue 

print({}.fromkeys(b,'PYTHON'))

#to specify differnt values in all fields
c= 'how are you doing'
dict1={}.fromkeys(c,'PYTHON')
for i in dict1:
	dict1[i]=c.count(i)
print(dict1)

#key can only be unique if you pass redundant values it will update with last values
dict2={'a':[23,43,343,46],'b':54}
print(dict2['a'][1])

#popitem : to rendomly remove data

print(dict2.popitem())
print(dict2)

#pop : to delete item based on key

#print(b.pop(34))
#'print(b)

#nested disctionary

dict3={'a':{23:43,343:46},'b':54}

print(dict3['a'][23])


#Get

dist4={'a':43,'b':89,'c':494,'d':545}

for i in dist4:
	print(dist4.get(i))


