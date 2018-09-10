
'''
Prompts the user for a seed for the random number generator,
and for a strictly positive number, nb_of_elements.
Generates a list of nb_of_elements random integers between 0 and 99, prints out the list,
computes the difference between the largest and smallest values in the list without using
the builtins min() and max(), prints it out, and check that the result is correct using
the builtins.
'''


from random import seed, randint
import sys


# Insert your code here
try:
    number_generator=int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer. Giving up.')
    sys.exit()
try:
    number_of_elements=int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer. Giving up.')
    sys.exit()
if number_of_elements<=0:
    print('Input should be strictly positive.')
    sys.exit()
seed(number_generator)
L=[randint(0,99) for _ in range(number_of_elements)]
print('\nThe list is:',L)
maxone=L[0]
minone=L[0]
for item in L:
    if item>maxone:
        maxone=item
    if item<minone:
        minone=item
print('\nThe maximum difference between largest and smallest values in this list is:',(maxone-minone))
print('Confirming with buildin operations:',max(L)-min(L))