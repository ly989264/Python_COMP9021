# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial

# Insert your code here
def get_input():
    try:
        number=int(input('Input a nonnegative integer: '))
    except ValueError:
        print('Incorrect input, giving up.')
        sys.exit()
    if number<0:
        print('Incorrect input, giving up.')
        sys.exit()
    # at least equals to 10 ???
    return number

def generate_factorial(number):
    result=1
    for i in range(1,number+1):
        result*=i
    return result

def first_method(number):
    result=generate_factorial(number)
    a,b=divmod(result,10)
    if b:
        return 0
    count=0
    while not b:
        count+=1
        a,b=divmod(a,10)
    return count

def second_method(number):
    string=str(generate_factorial(number))
    import re
    pattern=re.compile('^\d.*?(0*)$')
    result=re.match(pattern,string)
    if result:
        return len(result.group(1))
    else:
        return None

def third_method(number):
    result=generate_factorial(number)
    count=0
    while not result%5:
        result=result//5
        count+=1
    return count

# testing
# count=0
# for i in range(1,600):
#     number=i
#     result1=first_method(number)
#     result2=second_method(number)
#     result3=third_method(number)
#     if result1!=result2 or result1!=result3:
#         count+=1
# if count:
#     print('Error.')
# else:
#     print('Success.')

# output
the_input=get_input()
print(f'Computing the number of trailing 0s in {the_input}! by dividing by 10 for long enough:',
      first_method(the_input))
print(f'Computing the number of trailing 0s in {the_input}! by converting it into a string:',
      second_method(the_input))
print(f'Computing the number of trailing 0s in {the_input}! the smart way:',
      third_method(the_input))