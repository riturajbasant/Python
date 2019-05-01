'''
* * *
*   *
* * *
* *
*   *

***
  *
***
* *
* ***

'''

for i in range (5):
    if(i ==0 or i ==2):
        for j in range (3):
            print("*",end = " ")
        print()
    elif(i ==1 or i ==  4):
        for j in range(3):
            if (j==0 or j==2):
                print("*",end=" ")
            else:
                print(" ", end=" ")
        print()

    else:
         for j in range(3):
            if (j==0 or j==1):
                  print("*",end=" ")
            else:
                print(" ", end =" ")
         print()
    
    
