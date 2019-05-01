#file handling
'''
mode
1> w
2> r 
3> a
4> w+
5> r+ 
6> a+

#write mode
f= open('sample.txt','w') #It is used to create file sample.txt 
#if we are not not specifying anything it means it will be in read mode



f.write("hi python") #it will write hi python in sample.txt file

f.close()
f=read(sample.txt) #by default it is in read mode
f.seek(2)
f.close() #we can't use f variable after using close function




#code to count row number of file.
with open('sample.txt') as f:
	c=0
	for line in f:
		print(line)
		if(line.isspace()):
			c=c
		else:
		c=c+1
print(c)


#Append mode : it is used to add data in the already existing files and it will not delete the existing data and if file is not present it will create files as well.
#\n is used to add the data in new line
f=open('simple.txt','a')
f.write('grew grep fregds')


#read+ mode : it is used to read and write file. However, it will not create a new file and in read mode cursor is always on the first line of home page.
#it will also overwrite the data in file cursor by cursor.
#seek() is used to send the cursor the respected point line seek(10) it will start writing after 10 characters.
f=open('simple.txt','r+')
f.seek(10)
f.write('hello')
f.read() # is used to read the file 
f.close()


#how to find one word in file

for line in f:
	if(line.find('hello')):
		print("Hello")
f.close()



#write plus (w+) : it has same features of write plus read mode
f=open('simple.txt','w+')
print(f.read())
f.write('dkfsdklj asfjdsklj akfdjdkl jkdfj ksdj')
f.seek(0)
print(f.read())
f.close()


'''
#append+ : it is used to write and read file but cursor will be placed at the end. 









