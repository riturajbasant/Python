rang=int(input("Enter a range:"))
ctr=2
x=0
y=1
print(x,end=" ")
print(y,end=" ")
while True:
    temp=x
    x=y
    y=temp+y
    #X,Y = X ,X+Y
    print(y,end=" ")
    if(ctr==rang):
        break
    ctr=ctr+1
