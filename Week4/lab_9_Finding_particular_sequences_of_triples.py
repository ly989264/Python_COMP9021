# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers, i < j < k,
# every digit occurs at most once in i, j and k,
# and the product of i, j and k is a 6-digit number
# consisting precisely of the digits that occur in i, j and k.


# Insert your code here
import re
pattern=re.compile('^(\d)(\d)$')
def divide_integer_to_number(integer):
    number_list=[i for i in str(integer)]
    return number_list


def judge_list_duplicate(list1,list2):# if duplicate, return True; else return False
    for item in list1:
        if item in list2:
            return True
    return False

def check_itself(integer):
    result=re.match(pattern,str(integer))
    if result.group(1)==result.group(2):
        return False
    return True

for first_number in range(10,100):
    if not check_itself(first_number):
        continue
    first_number_list=divide_integer_to_number(first_number)
    for second_number in range(first_number,100):
        if not check_itself(second_number):
            continue
        second_number_list=divide_integer_to_number(second_number)
        if judge_list_duplicate(first_number_list,second_number_list):
            continue
        for third_number in range(second_number,100):
            if not check_itself(third_number):
                continue
            third_number_list=divide_integer_to_number(third_number)
            if judge_list_duplicate(first_number_list,third_number_list):
                continue
            if judge_list_duplicate(second_number_list,third_number_list):
                continue
            multi_result=first_number*second_number*third_number
            multi_result_list=divide_integer_to_number(multi_result)
            if len(multi_result_list)<6:
                continue
            befor_list=first_number_list+second_number_list+third_number_list
            count=0
            for item in befor_list:
                if item in multi_result_list:
                    count+=1
            if count==6:
                print(f'{first_number} x {second_number} x {third_number} = {multi_result} is a solution.')
