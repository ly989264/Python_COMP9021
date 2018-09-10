# Written by Eric Martin for COMP9021


'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between -50 and 50, prints out the list,
computes the mean, the median and the standard deviation in two ways,
that is, using or not the functions from the statistics module, and prints them out.
'''


from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
import sys


# Insert your code here
# get the input
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
    print('Input is not strictly positive, giving up.')
    sys.exit()

# generate the list
seed(number_generator)
L=[randint(-50,50) for _ in range(number_of_elements)]

# print out the list
print('\nThe list is:',L)
print('\n',end='')

# calculate the mean
sum=0
for item in L:
    sum+=item
meanvalue=sum/number_of_elements
print('The mean is %.2f.' %(meanvalue))

# calculate the median
# L.sort() is not a good choice here because it will change the list L, but we will need it later
new_L=sorted(L)
if number_of_elements%2==0:#even
    middle_index1=number_of_elements/2-1
    middle_index2=number_of_elements/2
    medianvalue=(new_L[int(middle_index1)]+new_L[int(middle_index2)])/2
else:
    middle_index=(number_of_elements-1)/2
    medianvalue=new_L[int(middle_index)]
print('The median is %.2f.' %(medianvalue))

#calculate the standard deviation
sum_of_square=0
for each in L:
    if each>meanvalue:
        temp=each-meanvalue
    else:
        temp=meanvalue-each
    sum_of_square+=temp*temp
standard_deviation_value=sqrt(sum_of_square/number_of_elements)
print('The standard deviation is %.2f.' %(standard_deviation_value))

# confirm with functions from the statistics module
print('\nConfirming with functions from the statistics module:')
print('The mean is %.2f.' %(mean(L)))
print('The median is %.2f.' %(median(L)))
print('The standard deviation is %.2f.' %(pstdev(L)))
