#function is way to reuse the fuctionality where we need.
#There are two types of function a) predefined fuctions and userdefined fuctions.
#functions contains some operations.
#first we define the fuctions by def keyword
#then we call the functions where we need.
#creating function without passing parameter.
'''
def sample():
	print("This is my function")

sample () #calling a function

#return type function
def add():
	x=10 #local veriable
	y=13 #local veriable
	return x+y # it will return x+y value to the add function.
	
add() # it will contain 23 as value
'''

#parameter 
#1 formal parameter
#2 actual parameter

#method to pass parameter into a function
'''
1. required argument
2. default argument
3. keyword argument
4. value-length argument
'

#required argument
def factorial (x): #formal parameter
	fact=1
	while(x>0):
		fact=fact*x
		x = x-1
	return fact
a=int(input("Enter a number: "))
factorial(a) #actual parameter



#default argument
def add (x,y=20): #default value of y is already 20
	return x+y
print(add(12))


#default argument
def add (x,y=20): #default value of y is already 20
	return x+y
print(add(x=12))


def add ():
	global x,y # to make variable global who can be assessible to all the functions
	
	x=int(input("Enter a number")) #local
	y = int(input("Enter a number ")) #local
	return x + y

def sub():
	return x-y
	
print(add())
print(sub())
print(x, y)


#keyword argument
def add (x,y):
	print(x+y)
add(x=12,y=23) #here we can't choose any other value like a , b ,c etc..


#value length argument

def func(x, *y): # *y will be considered as tuple and store values except first.
	print(x)
	sum=0
	print(y) # y will act as tuple who will store values of all the passed values
	for i in y :
		sum=sum+i
	print(sum)
func(23,43, 343,343,3,45,66,657)


#Dictionary creation

def func (**x):
	print(x)
	for i in x:
		print (i, ":", x[i])
func(a=12,b='FSV', c=877.544,d=98)

#inner function
def parent():
	print("In the parent function")
	global inner
	def inner():
		print("in the inner function")
	return inner ()
	
	
		
parent()
inner()
print(parent) #print hexadecimal id 
print(inner) #print hexadecimal id

print(id(parent)) # to print into ID format




#recursive function : to call function within function

def factorial (x):
	if(x==1):
		return 1
	else:
		return(x*factorial(x-1)) # factorial function will be called 
print(factorial(5))



#decorator function It used to functionality of extenal function without changing in the actual function. we create a inner function which is called rapper function.
#Wrapper function is used to wrap functionality of external function.

def decorator (fun):
	def wrapper():
		fun()
		fun()
		
	return wrapper
#extenal function
def add():
	x=10
	y=20
	print(x+y)
func=decorator(add)
func()



#decorator
def decorator (fun):
	def wrapper():
		fun()
		fun()
		
	return wrapper
#extenal function
def add():
	x=10
	y=20
	print(x+y)
func=decorator(add)
func()





#Generator : it will create generator object using yield keyword, generator object is also a iterable object but we can't iterate by index. Generator object uses
#next function for the iteration. Next function fetch one by one value from the generator
# we can't reuse generator values if we use one time of certain value.

def generator1(x):
	while (x>0):
		yield x
		x=x-1
		
print(generator1)
a=generator1(5) #if it fetches into list then it will stop iteration.
print(next(a))
print(list(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

'''

#Generator Expression

gen_exp= (x for x in range (5))
print(gen_exp)
print(next(gen_exp))
print(list(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))











































































