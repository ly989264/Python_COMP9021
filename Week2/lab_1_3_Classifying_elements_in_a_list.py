'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between 0 and 19, prints out the list,
computes the number of elements strictly less 5, 10, 15 and 20, and prints those out.
'''


from random import seed, randrange
import sys


# Insert your code here
try:
    number_generator=int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
try:
    number_of_elements=int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if number_of_elements<=0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
# generate the list
seed(number_generator)
L=[randrange(0,20) for _ in range(number_of_elements)]
# print out the list
print('\nThe list is:',L)
count_list=[0]*4
# 0-4, 5-9, 10-14, 15-19
# 0    1    2      3
# int(number/5)
for item in L:
    count_list[int(item/5)]+=1
# output
print('\n',end='')
for i in range(0,4):
    if count_list[i]==0:
        print('There is no element between ',i*5,' and ',(i+1)*5-1,'.',sep='')
    elif count_list[i]==1:
        print('There is 1 element between ',i*5,' and ',(i+1)*5-1,'.',sep='')
    else:
        print('There are ',count_list[i],' elements between ',i*5,' and ',(i+1)*5-1,'.',sep='')
