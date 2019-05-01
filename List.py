#List
'''
List is a standard datatypes
It is mutable. ie. we can change in list
it is defined under square brackets
list is the collection of different datatypes
Element of list will be seperated by comma
elements will be either string or integer or float

list1= [32,45, 78.34, 'huffh', 653]
print(list1)
print(type(list1))

list2=[98908,8908]
#concatenation
print(list1+list2)

#repeatation
print(list1*3)
#access
print(list1[2])
print(list1[-3])

#Slicing
print(list1[:])
print(list1[3:])
print(list1[:len(list1)])
print(list1[3:6])
#step
print(list1[0:len(list1):2])
#iteration
for i in list1:
	print(i)
#adding element in list
list1.append('jkdsjfjk')
print(list1)
#Finding value numbers
list1=[23,43,34,666,999,88]
print(list1)
even=[]
odd=[]
for i in list1:
	if(i%2==0):
		even.append(i)
	else:
		odd.append(i)
print(even)
print(odd)

#adding more than one value
list1=[32,343,334,3443,98]
print(list1)
list1.extend([543958490,'jlkfdls','0w9r0'])
print(list1)

print(id(list1))
list2=list1.copy()
print(list2)
print(id(list2))

del list1[2]
print(list1)

#Nested List
list3=[[34,343,34341,343],[898,434,3435]]
print(list3)

##update
list2=[54,343,343,32]
list2[1]=8
print(list2)

list3=[[34,343,34341,343],[898,434,3435]]
print(list3)
print(list3[0][1])

list2=[2,24,43,3435,5443]
for i, j in enumerate(list3):
	print(i, j)

list2=[2,24,43,3435,54,54,43,54,54,54]
list3=[[34,343,34341,343,[898,434,3435]]	
for i, j in zip(list3, list2):
	print(i, j)

list2=[2,24,43,3435,54,54,43,54,54,54]
for j in range(len(list2)):
	for i in list2:
		if(i==54):
			list2.remove(i)
print(list2)



#creation of list in one line
list1=input().split()
print(list1)

list2=[int(x) if (x.isdigit()) else x if (x.isalnum()) else float (x) for x in input().split()] 
print(list2)

list1= [x for x in range(1,6) if (x%2==0) if (x%4==0)]
print(list1)

'''

list4=[43,534,34,232,232,54]
list4.sort()
print(list4)