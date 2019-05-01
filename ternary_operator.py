#ternary operator
#1> simple method for ternary operator
'''
a= int(input("enter First Number")
b= int(input("Enter second number"))
c = a if a>b else b
print("largest number is ", c)
'''
'''
# tuple method for ternary operator
a = int(input("enter first Number: "))
b = int(input("enter Second Number: "))
c = ((b,a) [a>b])
print("largest number is ", c)

'''
'''
# Lamda expression method
a = int(input("enter first Number: "))
b = int(input("enter Second Number: "))
c = ((lambda:b,lambda:a) [a>b]())
print("Largest number is ", c)
'''
'''
#Dectionary Method
a = int(input("Enter  first number: "))
b = int(input("enter Second Number: "))
c = ({True:a, False:b}[a>b])
print("Largest Number is ", c)

'''

#Complex Method
a = int(input("Enter  first number: "))
b = int(input("enter Second Number: "))
c = int(input("enter Second Number: "))
print("a is greater" if a >b and a>c else "B is greater" if b>c else "C is greater")


