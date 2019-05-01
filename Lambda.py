#Lambda function
#it is an ananymous function
#it will operate on the list element by element
list2=[2,3,4,6,44,56,87]
a=lambda x:x**2
print(list(map(a,list2)))

b=lambda x:x%2==0
print(list(filter(b,list2)))



