# input: a list of numbers and a certain number
# output: several lists of numbers, the sum of all numbers of each list equals to the certain number

import re

def get_input():
    number_string=input('Please input the list of number, separated with one or more spaces: ')
    number_string=re.sub(' *','$',number_string)
    number_string=number_string.strip('$')
    number_list=number_string.split('$')
    for each_index in range(len(number_list)):
        number_list[each_index]=int(number_list[each_index])
    certain_number=input('Please input the number of sum: ')
    return number_list,int(certain_number)

def operate(number_list,certain_number,list):
    global final_list
    if certain_number==0:
        list.sort()
        final_list.append(list)
        return
    if certain_number<0:
        return
    if len(number_list)==0:
        return
    for each_index in range(len(number_list)):
        # print(number_list[0:each_index]+number_list[each_index+1:],certain_number-number_list[each_index])
        result=operate(number_list[0:each_index]+number_list[each_index+1:],certain_number-number_list[each_index],list[:]+[number_list[each_index]])

def sort_key(x):
    return tuple(x)


number_list,certain_number=get_input()
final_list=[]
for each_index in range(len(number_list)):
    result=operate(number_list[0:each_index]+number_list[each_index+1:],certain_number-number_list[each_index],[number_list[each_index]])
already_l=[]

result_dict={}
for each_element in final_list:
    if len(each_element) not in result_dict.keys():
        result_dict[len(each_element)]=[each_element]
    else:
        result_dict[len(each_element)].append(each_element)
for each_key in result_dict.keys():
    result_dict[each_key].sort(key=sort_key)
key_list=[]
for each_key in result_dict.keys():
    key_list.append(each_key)
key_list.sort()
final_list=[]
for each_key in key_list:
    for each_element in result_dict[each_key]:
        final_list.append(each_element)
# final_list.sort(key=lambda x: len(x))
for each_pair in final_list:
    temp_set=set(each_pair)
    if temp_set in already_l:
        continue
    already_l.append(temp_set)
    each_pair.sort()
    print(each_pair)