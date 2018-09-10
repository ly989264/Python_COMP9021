# IMPLEMENT THE ELEMENTARY CELLULAR AUTOMATA
import sys

def get_rule():
    '''
    get an integer from 0 to 255 from the input, check its validity and return the valid value
    :return: rule_number<integer>
    '''
    try:
        rule_number=int(input('Please input an integer from 0 to 255: '))
    except ValueError:
        print('Invalid input, giving up.')
        sys.exit()
    if rule_number<0 or rule_number>255:
        print('The number you input is not in the correct range.')
        response=input('Is it okay to use its mod value? (Y or N) ')
        if response=='Y':
            mod_number=rule_number%256
            return mod_number
        else:
            print('Invalid input, giving up.')
            sys.exit()
    else:
        return rule_number

def generate_rule_dict(rule_number):# not familiar with this function, practice more
    '''
    generate the rule dict from the rule number passed
    :param rule_number: integer, returned from the get_rule() function
    :return: rule_dict<{(0,0,0):int,(0,0,1):int,...}>
    '''
    rule_dict={}
    tuple_list=[(i//4,i//2%2,i%2) for i in range(7,-1,-1)]
    rule_number_binary_str=f'{rule_number:08b}'
    for i in range(0,8):
        rule_dict[tuple_list[i]]=int(rule_number_binary_str[i])
    return rule_dict

def initial_pair():
    '''
    initialize the first pair, which is (0,1), representing the outside is 0 and the inside is an only 1
    :return: tuple<(0,1)>
    '''
    return (0,1)

def calculate_the_next_pair(rule_dict,current_pair):
    '''
    calculate the next pair from the current pair
    through adding two first element of the current pairs at the first as well as the last the the current pair
    :param rule_dict: dict<{(0,0,0):int,(0,0,1):int,...}>
    :param current_pair: tuple<(outsider,insider_line)>
    :return: the next pairs: tuple<(outsider,insider_line)>
    '''
    next_list = []
    current_list=[current_pair[0],current_pair[0]]
    for i in current_pair:
        current_list.append(i)
    current_list.append(current_pair[0])
    current_list.append(current_pair[0])
    length_of_current_list=len(current_list)
    for each_first_item in range(0,length_of_current_list-2):
        next_list.append(rule_dict[(current_list[each_first_item],current_list[each_first_item+1],current_list[each_first_item+2])])
    next_pair=tuple(next_list)# convert list to tuple can simply use tuple() function
    return next_pair

def display_certain_line(tuple,length):
    '''
    given a certain tuple with the format(outsider,insider...), display the list with 1 in black block and 0 in white block
    :param tuple: a certain tuple with the format (outsider,insider...)
    :param length: length at either side
    :return: no certain return
    '''
    outsider=tuple[0]
    insider_list=[outsider]*length
    for i in range(1,len(tuple)):
        insider_list.append(tuple[i])
    for _ in range(0,length):
        insider_list.append(outsider)
    for eachchar in insider_list:
        if eachchar==1:
            print('\U000025a0',end='')
        else:
            print('\U000025a1',end='')
    print()
    return

def main():
    rule_number=get_rule()
    rule_dict=generate_rule_dict(rule_number)
    current_pair=initial_pair()
    display_certain_line(current_pair,50)
    length=50
    for i in range(1,50):
        new_pair=calculate_the_next_pair(rule_dict,current_pair)
        del current_pair
        current_pair=new_pair
        # print(new_pair)
        display_certain_line(new_pair,length-i)

if __name__=='__main__':
    main()
