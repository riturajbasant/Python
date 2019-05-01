'''
rang=int(input("Enter a range:"))
ctr=1
sum_even=0
sum_odd=0
while True:
    if(ctr%2==0):
        print(ctr,"is a even number")
        sum_even=sum_even+ctr

    else:
        print(ctr,"is an odd number")
        sum_odd=sum_odd+ctr

    ctr=ctr+1
    if(ctr==rang+1):
        break
print("Sum of even numbers upto range %d is %d"%(rang,sum_even))
print("Sum of odd numbers upto range %d is %d"%(rang,sum_odd))
'''
'''
ctr=1
while(ctr<=10):
    print(ctr,end=" ")
    if(ctr==5):
        break
    print("hello")
    ctr=ctr+1
 '''

# factorial
# 5!=5*4*3*2*1
'''
num = int(input("Enter a number:"))
fact=1
while(num>0):
    fact=fact*num
    print(num,end="*")
    num=num-1
print("\nFactorial is %d"%fact)

 '''
x=0
if(not x):
    print("hello")
else:
    print("No hello")














