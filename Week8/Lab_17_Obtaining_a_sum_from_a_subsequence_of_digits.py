# Prompts the user for two numbers, say available_digits and desired_sum, and
# outputs the number of ways of selecting digits from available_digits
# that sum up to desired_sum.

# NEED TO THINK AGAIN

import sys

# Insert your code here
def get_numbers():
    try:
        available_digits=int(input('Input a number that we will use as available digits: '))
        desired_sum=int(input('Input a number that represents the desired sum: '))
        if available_digits < 0 or desired_sum < 0:
            raise ValueError
    except ValueError:
        print('Invalid input.')
        sys.exit()
    return available_digits,desired_sum

def save_digits_in_dict(available_digits):
    result_dict={}
    available_digits_string=str(available_digits)
    for each_element in available_digits_string:
        each_digit=int(each_element)
        if each_digit in result_dict.keys():
            result_dict[each_digit]+=1
        else:
            result_dict[each_digit]=1
    return result_dict

def save_digits_in_list(available_digits):
    return [int(i) for i in str(available_digits)]

def operate(result_list,desired_sum):
    sum=0
    if not desired_sum:
        return []
    if not result_list:
        return 'Error'
    for each_element in result_list:
        sum+=each_element
    if sum < desired_sum:
        return 'Error'
    flag=False
    for each_element in result_list:
        if each_element<=desired_sum:
            flag=True
    if not flag:
        return 'Error'
    current_new_list=[]
    for each_remove in result_list:
        if each_remove > desired_sum:
            continue
        temp_list=[]
        n_list=result_list[:]
        n_list.remove(each_remove)
        new_list=operate(n_list,desired_sum-each_remove)
        if new_list=='Error':
            continue
        elif new_list:
            for each_list in new_list:
                temp_list=[]
                for each_element in each_list:
                    temp_list.append(each_element)
                temp_list.append(each_remove)
                current_new_list.append(temp_list)
        else:
            temp_list.append(each_remove)
            current_new_list.append(temp_list)
    return current_new_list

def final_operate(result_dict,current_new_list):
    if current_new_list=='Error':
        return 0
    sum=0
    set_of_tuple=set()
    for each_result in current_new_list:
        a_list=each_result[:]
        a_list.sort()
        a_tuple=tuple(i for i in a_list)
        set_of_tuple.add(a_tuple)
    for each_tuple in set_of_tuple:
        nb_of_multi=1
        little_dict={}
        for each_char in each_tuple:
            if each_char in little_dict.keys():
                little_dict[each_char]+=1
            else:
                little_dict[each_char]=1
        for each_key in little_dict.keys():
            if little_dict[each_key]!=result_dict[each_key]:
                minus=result_dict[each_key]-little_dict[each_key]
                nb_of_multi*=(minus+1)
        sum+=nb_of_multi
    return sum
    # final_dict={}
    # for each_current_working_sub_list in current_new_list:
    #     a_list=each_current_working_sub_list[:]
    #     a_list.sort()
    #     tuple_of_each_current_working_sub_list=tuple(i for i in a_list)
    #     if tuple_of_each_current_working_sub_list in final_dict.keys():
    #         final_dict[tuple_of_each_current_working_sub_list]+=1
    #     else:
    #         final_dict[tuple_of_each_current_working_sub_list]=1
    # # print(final_dict)
    # for each_key in final_dict:
    #     little_dict={}
    #     nb_of_multi=1
    #     for each_letter in each_key:
    #         if each_letter in little_dict.keys():
    #             little_dict[each_letter]+=1
    #         else:
    #             little_dict[each_letter]=1
    #     count=0
    #     for each_letter in little_dict.keys():
    #         if little_dict[each_letter]!=result_dict[each_letter]:
    #             current_multi=result_dict[each_letter]
    #             if current_multi>nb_of_multi:
    #                 nb_of_multi=current_multi
    #         else:
    #             count+=1
    #     final_dict[each_key]=final_dict[each_key]//nb_of_multi
    #     if count==len(little_dict):
    #         final_dict[each_key]=1
    # print(final_dict)
    # sum=0
    # for each_value in final_dict.values():
    #     sum+=each_value
    # return sum


available_digits,desired_num=get_numbers()
result_dict=save_digits_in_dict(available_digits)
# print(result_dict)
result_list=save_digits_in_list(available_digits)
current_new_list=operate(result_list,desired_num)
# print(current_new_list)
sum=final_operate(result_dict,current_new_list)
# print(current_new_list)
# print(current_new_list)
if sum==0:
    print('There is no solution.')
elif sum==1:
    print('There is a unique solution.')
else:
    print(f'There are {sum} solutions.')
