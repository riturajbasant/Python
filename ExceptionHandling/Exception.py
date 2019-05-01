#exception Handling 
#exception
#print(1/0)
#Type Error

'''

a=10
b='20'
print(a+b)


#File not found error

f=open('fbet.txt')
f.close()

#Module not found error

import adfjlksj



# file already exist error

import os
os.mkdir('pack')
'''

#keywords in exception handling

#1 try 2 exception 3 finally 4 raise


try:
    a = int(input('Enter first value'))
    b=int(input("Enter the second value : "))
    print ("Division of first try ", a/b)
    try:
        print('Division is ', b/a)
    except:
        print("we can not devide an integer first number is  zero")

except:
    print("We can't devide an integer by second number is  zero")


