'''
f1 = open('C://users/ritu.basant/DesktopVocablary.txt', 'r')
f = open('new.txt', 'w')
#f1.write('Helo how arey you')


for data in f1:
	f.write(data)

#print(f.readline())

'''

with open('Practice.txt','r') as f:

	for data in f:
		a = open('newfile.txt','a')
		a.write(data)
		
		 
	