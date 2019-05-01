#if elif else statement
'''
if(condition):
    block
elif(condition):
    block
elif(condition):
    block
elif(condition):
    block
----------------
-----------------
----------------
else:
    block:
'''
#Ex--Resturent item
#chowmin = 30
rate_chowmin = 30
rate_momos = 20
rate_chilly=40
rate_mixveg=50
print("Press 1 for order chowmin")
print("Press 2 for order momos")
print("press 3 from order chilly")
print("press 4 for order mixweg")
item = int(input("Enter item code"))

if(item == 1):
    print("Rate of chowmin", rate_chowmin)
elif(item == 2):
    print("Rate of momos", rate_momos)
elif(item == 3):
    print("Rate of chilly", rate_chilly)
elif(item == 4):
    print("Rate of mixveg", rate_mixveg)
else:
    print("wrong input")
