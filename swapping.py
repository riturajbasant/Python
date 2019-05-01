#swapping of two numbers
'''
a = int(input("enter value of A :"))
b = int(input("enter value of B :"))
a, b=b,a
print("value of a is ", a)
print("Value of B is ", b)

'''
'''
#temporary variable method
a = int(input("enter value of A :"))
b = int(input("enter value of B :"))
temp = b
b=a
a =temp
print("Value of A ", a)
print("value of B ", b)
'''
#Arithmetic Method

a = int(input("enter value of A :"))
b = int(input("enter value of B :"))
a = a+b 
b = a-b 
a= a-b
print("Value of A ", a)
print("value of B ", b)



