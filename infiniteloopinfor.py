#Making infinate loop

#repeat function is used to repeat a word and creates infinite loop
'''
ctr = 0
from itertools import repeat

for i in repeat('hello'):
    print(i)
    ctr+= 1
    if ctr ==10:
        break


'''
'''
#it will repeat the list till infinity

ctr = 0
from itertools import cycle

for i in cycle(['winter', 'summer', 'autoum', 'rainy']):
    print(i)
    ctr+= 1
    if ctr ==10:
        break

        '''

#count also work as infinite loop here 0 is start and 2 is step. There is no end in counnt and it will work infinite


from itertools import count

ctr = 0

for i in count(0, 2):
    print(i)
    ctr+= 1
    if ctr ==10:
        break


#
