# Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.



# Insert you code here

import sys

def get_number():
    '''
    get the nonnegative number from the input
    :return: nonnegative integer
    '''
    try:
        number=int(input('Enter a nonnegative integer: '))
        if number<0:
            raise ValueError
    except ValueError:
        print('Invalid input value, giving up.')
        sys.exit()
    return number

def generate_dict(number):
    '''
    generate a dictionary of pascal triangle of number+1 lines
    :param number:nonnegative integer
    :return:a dictionary with the format {1:[1],2:[1,1]...}
    '''
    value_dict={}
    value_dict[1]=[1]# generate the first line
    if number>=1:
        value_dict[2]=[1,1]# generate the second line if number is larger or equal to 1
    if number<=1:
        return value_dict
    for eachlinenumber in range(3,number+2):
        value_dict[eachlinenumber]=[]
        value_dict[eachlinenumber].append(1)
        for eachinsideelement in range(1,eachlinenumber-1):
            value_dict[eachlinenumber].append(value_dict[eachlinenumber-1][eachinsideelement-1]+value_dict[eachlinenumber-1][eachinsideelement])
        value_dict[eachlinenumber].append(1)
    return value_dict

def nicely_display(value_dict,number):
    '''
    nicely display the pascal triangle value_dict contains
    :param value_dict:a dictionary with the format {1:[1],2:[1,1]...}
    :param number:nonnegative integer
    :return:None
    '''
    max_length_of_number=len(str(value_dict[number+1][number//2]))
    width=max_length_of_number
    largest_space_pack_before=number
    for eachkey in value_dict.keys():
        space_pack_before=largest_space_pack_before-eachkey+1
        print(' '*space_pack_before*width,end='')
        for eachelementindex in range(0,len(value_dict[eachkey])-1):
            print(f'{value_dict[eachkey][eachelementindex]:{width}}',end='')
            print(' '*width,end='')
        print(f'{value_dict[eachkey][-1]:{width}}')
    return

number=get_number()
value_dict=generate_dict(number)
nicely_display(value_dict,number)
