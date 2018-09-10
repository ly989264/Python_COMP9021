# Prompts the user for a strictly positive number N
# and outputs an equilateral triangle of height N.
# The top of the triangle (line 1) is labeled with the letter A.
# For all nonzero p < N, line p+1 of the triangle is labeled
# with letters that go up in alphabetical order modulo 26
# from the beginning of the line to the middle of the line,
# starting wth the letter that comes next in alphabetical order
# modulo 26 to the letter in the middle of line p,
# and then down in alphabetical order modulo 26
# from the middle of the line to the end of the line.


# Insert your code here

import sys

def get_positive_number():
    '''
    get a positive number from the input, check it and return it
    :return: integer
    '''
    try:
        number=int(input('Enter strictly positive number: '))
        if number <= 0:
            raise ValueError
    except ValueError:
        print('Invalid input value, giving up.')
        sys.exit()
    return number

def convert_number_to_upper_letter(number):
    '''
    convert the number of 0 to 25 to upper letter
    :param number: integer
    :return: upper letter
    '''
    actual_number=number+65
    return chr(actual_number)

def generate_dict(number):
    '''
    generate a dictionary using the given number
    :param number: integer
    :return: a dictionary contains the numbers of first half part of eachline
    '''
    value_dict={}
    current_integer=0
    for linenumber in range(1,number+1):
        value_dict[linenumber]=[]
        for eachletternumber in range(0,linenumber):
            value_dict[linenumber].append(current_integer)
            current_integer+=1
            if current_integer==26:
                current_integer=0
    return value_dict

def draw_picture(value_dict,number):
    '''
    using the given value dictionary to draw the picture
    using the number parameter to help the output nicely
    :param value_dict: a dictionary contains the numbers of first half part of eachline
    :param number: the number of line
    :return: no return value
    '''
    largest_spaces=number# pay attention that the first key is 1, so the largest_spaces should be the number
    for eachkey in value_dict.keys():
        actual_spaces=largest_spaces-eachkey
        empty_string=' '*actual_spaces
        if eachkey==1:
            print(empty_string,convert_number_to_upper_letter(value_dict[eachkey][0]),sep='')
        else:
            print(empty_string,end='')
            for eachelement in range(0,len(value_dict[eachkey])-1):
                print(convert_number_to_upper_letter(value_dict[eachkey][eachelement]),end='')
            print(convert_number_to_upper_letter(value_dict[eachkey][-1]),end='')
            for eachconverseelement in range(-2,-len(value_dict[eachkey])-1,-1):# pay attention: starts with the index -2 and the last one should be -len()
                print(convert_number_to_upper_letter(value_dict[eachkey][eachconverseelement]),end='')
            print()
    return

number=get_positive_number()
value_dict=generate_dict(number)
draw_picture(value_dict,number)
