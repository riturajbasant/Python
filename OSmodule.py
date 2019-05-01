import os
#for current path
#print(os.getcwd())
'''
#change the path
os.chdir('..')

print(os.getcwd())

os.chdir('Python')
print(os.getcwd())
#How to give specific path

#\\ works similar to /
os.chdir('C:\\Users\\ritu.basant\\Desktop\\Python\\OS Module')

# We can also specify like below

os.chdir('C:/Users/ritu.basant/Desktop/Python/OS Module')
print(os.getcwd())

print(os.getcwd())
#os.mkdir('package')
print(os.getcwd())
os.chdir('package')
f=open('test.txt','w')
f.write("Hello python")
f.close()
os.chdir('..')
print(os.getcwd())
#os.rmdir('package')
os.chdir('package')
os.remove('test.txt')
os.chdir('..')
os.rmdir('package')

'''