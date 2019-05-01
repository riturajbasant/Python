try:
    a=input("Enter first value : ")
    b=input("Enter the second Value : ")
    if(not a.isdigit() or not b.isdigit()):
        raise TypeError
    else:
        a=int(a)
        b=int(b)
        c=a+b
        print("Sum of a and b is ", c)
except TypeError:
    print(TypeError)