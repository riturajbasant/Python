'''
x = int(input("Enter Year"))

def leapyear():
    if(x %400==0 or x % 4==0):
    
        print( x, " is leap year")
    elif(x%100==0):
        print(x, "Is not a  leap year")
        
    else:
        print(x, "is not a leap year")

leapyear()
'''
x = int(input("Enter Year"))
if(x%4==0):
        if(x%100==0):
            if(x%400==0):
                print(x,"is aleap year")
            else:
                print(x,"is not a leap year")
        else:
            print(x,"is a leap year")
else:
    print(x,"is not aleap year")
                

