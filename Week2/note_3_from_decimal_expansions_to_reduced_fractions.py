import re

def compute_fraction(sigma,tau):# pay attention: sigma and tau are both strings
    if re.match('^.*?str.*$',str(type(sigma))) and re.match('^.*?str.*$',str(type(tau))):
        pass
    else:
        print('Invalid type of arguments inputted.')
        return None
    pattern=re.compile('^\d+$')
    if re.match(pattern,sigma) and re.match(pattern,tau):
        pass
    else:
        print('Invalid sigma and tau inputted.')
        return None
    numerator=int(sigma)*(10**len(tau)-1)+int(tau)
    denominator=(10**len(tau)-1)*10**len(sigma)
    return numerator,denominator
    # but the compute_fraction function has a problem, that is if I want to input 0.142857...,
    # I don't know how to assign to the sigma

def gcd(number1,number2):
    if number1>0 and number2>0:
        pass
    else:
        print('Nonsense of calculating the gcd of two numbers, within which a number is not strictly positive.')
        return None
    while number2:
        number1,number2=number2,number1%number2
    return number1

def reduce_two_numbers(number1,number2):
    gcd_of_two=gcd(number1,number2)
    if gcd_of_two:
        return number1//gcd_of_two,number2//gcd_of_two
    else:
        return None

# execution
# format: 0.sigmatau...
total_string=input('Please input the string with the format of "0.x/y...", within which the y is the repeated section.\n'
                   'Here is your input: ')
total_pattern=re.compile('^0\.(\d+)/(\d+)\.\.\.$')
total_result=re.match(total_pattern,total_string)
while True:
    if total_result:
        sigma=total_result.group(1)
        tau=total_result.group(2)
        break
    else:
        print('Something wrong with your input. Try again!')
        total_string = input(
            'Please input the string with the format of "0.x/y...", within which the y is the repeated section.\n'
            'Here is your input: ')
        total_result = re.match(total_pattern, total_string)
compute_fraction_result=compute_fraction(sigma,tau)
if compute_fraction_result:
    numerator,denominator=compute_fraction_result
reduce_two_numbers_result=reduce_two_numbers(numerator,denominator)
if reduce_two_numbers_result:
    final_numerator,final_denominator=reduce_two_numbers_result
print('%d/%d' %(final_numerator,final_denominator))