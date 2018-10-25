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

def operate(number_list, index, desired_number,list):
    global final_list
    if desired_number==0:
        final_list.append(list)
        return
    if desired_number<0:
        return
    if index==len(number_list)-1:
        return
    for i in range(index+1,len(number_list)):
        operate(number_list,i,desired_number-number_list[i],list+[number_list[i]])


number_list,desired_number=get_input()
length_of_number_list=len(number_list)
final_list=[]
for each_index in range(length_of_number_list):
    operate(number_list,each_index,desired_number-number_list[each_index],[number_list[each_index]])
print(len(final_list))