# Prompts the user for an integer N and finds all perfect numbers up to N.
# Quadratic complexity, can deal with small values only.


import sys

# Insert your code here
def get_number():
    try:
        number=int(input('Input an integer: '))
    except ValueError:
        print('Incorrect input, giving up.')
        sys.exit()
    if number<=0:
        print('Incorrect input, giving up.')
        sys.exit()
    return number

def get_perfect_number_smaller_or_equal(n):
    for each in range(2,n+1):
        sum=0
        for i in range(1,each):
            if not each%i:
                sum+=i
        if sum==each:
            print(f'{each} is a perfect number.')

number=get_number()
get_perfect_number_smaller_or_equal(number)