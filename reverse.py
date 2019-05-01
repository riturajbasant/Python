# Reverse of the program
# 123=321
'''
num=int(input("Enter a number"))
n=num
rev=0
while(num>0):
	rem = num%10
	rev = rev*10 + rem
	num=num//10
print("Reverse of the %d is %d"%(n,rev)) 	
'''
# prime number
# ex-2,3,5,7,11,13,17,19.....
'''
num=int(input("Enter a number:"))
ctr=2
flag=1
while(ctr<num):
	if(num%ctr==0):
		flag=0
	if(flag==0):
		break
	ctr=ctr+1	
if(flag==1 and num>1):
	print(num,"is a prime number")
else:
	print(num,"is not a prime number")
'''
# palindrome number\
'''
num=int(input("Enter a number"))
n=num
rev=0
while(num>0):
	rem = num%10
	rev = rev*10 + rem
	num=num//10
print("Reverse of the %d is %d"%(n,rev))
if(rev==n):
	print(n,"is a palindrome number")
else:
	print(n,"is not a palindrome number")
'''
# armstrong number
#153=1**3 + 5**3 + 3**3
rang=int(input("Enter a rang:"))
ctr=0
num=1
while True:
	n=num
	lent=len(str(num))
	sum=0
	while(num>0):
		rem = num%10
		sum=sum+rem**lent
		num=num//10
	if(sum==n):
		print(n,end=" ")
		ctr=ctr+1
	if(ctr==rang):
		break
	num=n	
	num=num+1






	