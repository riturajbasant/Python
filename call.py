

'''import sys

#Normal calling of attributes from package exceptionhandling 
sys.path.append("C:\\Users\\ritu.basant\\Desktop\\Python\\")


#from ExceptionHandling import sub

from ExceptionHandling import *

print(sum1)
add()
show()
sub()

even()
odd()
'''

#Now we only want to access user module and don't want to access other modules
import sys

#Normal calling of attributes from package exceptionhandling 
sys.path.append("C:\\Users\\ritu.basant\\Desktop\\Python\\")


from ExceptionHandling import *

#to excplicity call user1 methods as we have only called user through __init__.py file
from ExceptionHandling.user1 import *
print(user.sum1)
user.sub()
user.show()
user.add()
even()
odd()


