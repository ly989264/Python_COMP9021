# Given a digit string excluded 01, return all possible letter combinations that the number could represent.

import sys

library={
    2:['a','b','c'],
    3:['d','e','f'],
    4:['g','h','i'],
    5:['j','k','l'],
    6:['m','n','o'],
    7:['p','q','r','s'],
    8:['t','u','v'],
    9:['w','x','y','z']
}

def get_input():
    number_string=input('Give me the string of numbers: ')
    number_list=[]
    for each_char in number_string:
        if each_char=='1' or each_char=='0':
            print('Invalid input.')
            sys.exit()
        number_list.append(int(each_char))
    return number_list

def get_combinations(number_list,list):
    global library
    global final_list
    if not number_list:
        final_list.append(list)
        return
    current_number=number_list[0]
    corresponding_list=library[current_number]
    for each_letter in corresponding_list:
        temp=[]
        for each_element in list:
            temp.append(each_element)
        temp.append(each_letter)
        get_combinations(number_list[1:],temp)
    return

# testing
final_list=[]
number_list=get_input()
get_combinations(number_list,[])
for each_element in final_list:
    print(each_element)
print(len(final_list))