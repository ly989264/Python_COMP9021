# input: a list of numbers and a certain number
# output: several lists of numbers, the sum of all numbers of each list equals to the certain number

import re

def get_input():
    number_string=input('Input a number that we will use as available digits: ')
    number_list=[]
    for each_char in number_string:
        number_list.append(int(each_char))
    desired_number=int(input('Input a number that represents the desired sum: '))
    return number_list,desired_number

def operate(desired_number,number):
    global number_dict
    nb=0
    if desired_number==0:
        return 1
    if desired_number<0:
        return 0
    for largest_number in range(number,0,-1):
        if largest_number not in number_dict.keys():
            continue
        nb_of_large = number_dict[largest_number]
        for i in range(1,nb_of_large+1):
            sum_of_small=desired_number-largest_number*i
            nb_of_small=operate(sum_of_small,largest_number-1)
            nb+=(nb_of_large-i+1)*nb_of_small
            # print(largest_number,nb_of_large,nb_of_small)
    return nb

number_list,desired_number=get_input()
number_dict={}
for each_number in number_list:
    if each_number in number_dict.keys():
        number_dict[each_number]+=1
    else:
        number_dict[each_number]=1
count=operate(desired_number,desired_number)
# print(number_dict)
print(count)
