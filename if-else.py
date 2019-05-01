#nested if statement

'''
syntex:
if(condition):
    if(condition):
        block
    else:
        block
else:
    block
'''

# detecting nunber is either zero or negative or positive

num = int(input("Enput numer "))
if(num>=0):
    if(num==0):
        print("number is zero")
    else:
        print("Number is positive")

else:
    print("Number is negative")
    
