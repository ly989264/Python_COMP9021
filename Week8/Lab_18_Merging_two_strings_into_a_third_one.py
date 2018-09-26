# Say that two strings s_1 and s_2 can be merged into a third
# string s_3 if s_3 is obtained from s_1 by inserting
# arbitrarily in s_1 the characters in s_2, respecting their
# order. For instance, the two strings ab and cd can be merged
# into abcd, or cabd, or cdab, or acbd, or acdb..., but not into
# adbc nor into cbda.
#
# Prompts the user for 3 strings and displays the output as follows:
# - If no string can be obtained from the other two by merging,
# then the program outputs that there is no solution.
# - Otherwise, the program outputs which of the strings can be obtained
# from the other two by merging.


# Insert your code here

import re

def operate(a_list,b_list,c_list):
    global flag
    if not a_list:
        flag=True
        return
    if not b_list:
        for each_index in range(len(a_list)):
            if a_list[each_index]!=c_list[each_index]:
                return
            flag=True
            return
    if not c_list:
        for each_index in range(len(a_list)):
            if a_list[each_index]!=b_list[each_index]:
                return
            flag=True
            return
    temp_a=a_list.pop(0)
    if b_list[0]!=temp_a and c_list[0]!=temp_a:
        return
    elif b_list[0]==temp_a and c_list[0]!=temp_a:
        b_list.pop(0)
        operate(a_list,b_list,c_list)
    elif b_list[0]!=temp_a and c_list[0]==temp_a:
        c_list.pop(0)
        operate(a_list,b_list,c_list)
    else:
        operate(a_list,b_list[1:],c_list)
        operate(a_list,b_list,c_list[1:])

first_string=input('Please input the first string: ')
second_string=input('Please input the second string: ')
third_string=input('Please input the third string: ')
string_list=[first_string,second_string,third_string]
string_list.sort(key=lambda x:len(x))
string_list.reverse()
a_list=[i for i in string_list[0]]# longest
b_list=[i for i in string_list[1]]
c_list=[i for i in string_list[2]]
flag=False
operate(a_list,b_list,c_list)
if flag:
    if first_string==string_list[0]:
        print('The first string can be obtained by merging the other two.')
    elif second_string==string_list[0]:
        print('The second string can be obtained by merging the other two.')
    else:
        print('The third string can be obtained by merging the other two.')
else:
    print('No solution')