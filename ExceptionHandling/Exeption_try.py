try:
    a =10
    b='20'
    try:
        c=a+b
    except TypeError as t:
        print(t)
    finally:
        print("this is Nested finally")
    f=open('dgreg.txt','w')
   # print(f.read())
except FileNotFoundError as f: 
    #here we are storing error message of Filenotfounderror and storing it as f and printing the same
    print(f)

    #Finally is executed weather try or except runs or not, Finally by default executed or it is generally used to 
    #close the resources.
#finally is used with Try statement

finally:
    f.close()
    print("this is finally statement")
    