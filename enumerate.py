# enumerate is a predefined function and it will return index as well as values
# we will pass a sequence as  a parameter in enumberate


'''
for i, j in enumerate (range (4,30,2)):
    print(i,j)
'''

#zip

for i, j in zip(range(4,10,1), range(1,6)):
    print(i, "+", j, "=", i +j)
