import os

#how to check attributes and methods of modules

print(os.getcwd())

os.chdir('C:/Users/ritu.basant/Desktop/Python/OS Module')
print(os.getcwd())

os.mkdir('os-test')
os.makedirs("os-test/file/new/x/y/z")

#os.rmdir('os-test')
os.removedirs("/file/new/x/y/z")

os.rename('test.txt''demo.txt') #first source file and then newfilename