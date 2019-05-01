print("Hello I am init")
'''
This is used to import modules from init file

from ExceptionHandling.user import *
from ExceptionHandling.user import sub

from ExceptionHandling.User1 import *
'''

#Now we only want to import only one module or file "user" in package

__all__ = ['user']