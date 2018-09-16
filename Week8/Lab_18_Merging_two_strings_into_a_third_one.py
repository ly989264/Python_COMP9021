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

def get_three_strings():
    first_string=input('Please input the first string: ')
    second_string=input('Please input the second string: ')
    third_string=input('Please input the third string: ')
    return first_string,second_string,third_string

def check_merge(target_string,source_string_1,source_string_2):
    source_2_list=[]
    for each_element in source_string_2:
        source_2_list.append(each_element)
    length_of_source_string_2=len(source_string_2)
    # nb of empty block=length_of_source_string_2+1
    pattern_string=r'^(.*?)'
    for i in range(len(source_2_list)):
        pattern_string+=source_2_list[i]
        pattern_string+=r'(.*?)'
    pattern_string+=r'$'
    pattern=re.compile(pattern_string)
    result=re.match(pattern,target_string)