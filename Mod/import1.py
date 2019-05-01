#package in the folder in which modules exist
#module is collection of functions and classes

import sys
sys.path.append('C:/Users/ritu.basant/Desktop/Python')

from Mod import userdefinedmodule as t
print("Press 1 for the factorial.")
print("Press 2 for square Root")
choice=input("Enter your choice:")
if(choice=='1'):
	x=int(input("Enter a number"))
	print("Factorial of %d is %d"%(x,t.factorial(x)))
elif (choice == '2'):
	x=int(input("Enter a number:"))
	print("Square root of %d is %f"%(x,t.sqt(x)))
else:
	print("Invalid choice")


