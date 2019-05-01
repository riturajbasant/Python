try:
    a=input("enter the Fist Value ")
    b=input("Enter the second Value")
    if(not a.isdigit() or not b.isdigit()):
        raise TypeError
    elif (b=='0'):
        raise ZeroDivisionError
    else:
        a=int(a)
        b=int(b)
        c=a+b
        d=a/b
        print("Sum of a and b is ", c)
        print("Division of %.2f by %.2f : %.2f" %(a,b,d))

except TypeError:
    print(TypeError)
except ZeroDivisionError:
    print(ZeroDivisionError)