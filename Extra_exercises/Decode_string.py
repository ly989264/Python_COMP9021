# Given an expression s includes numbers, letters and brackets.
# Number represents the number of repetitions inside the brackets(can be a string or another expression)．
# Please expand expression to be a string.
# s = abc3[a] return abcaaa
# s = 3[abc] return abcabcabc
# s = 4[ac]dy, return acacacacdy
# s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz

from Stack_adt import *

def decode_string(string):
    stack=Stack()
    for each_char in string:
        if each_char != ']':
            stack.push_in_stack(each_char)
        else:
            temp_list=[]
            while stack.read_last_element() is not None:
                temp=stack.read_last_element()
                if temp=='[':
                    stack.pull_out_stack()
                    break
                temp_list.append(stack.pull_out_stack())
            multi=stack.pull_out_stack()
            temp_list.reverse()
            for _ in range(int(multi)):
                for each_element in temp_list:
                    stack.push_in_stack(each_element)
    final_list=[]
    while stack.read_last_element() is not None:
        final_list.append(stack.pull_out_stack())
    final_list.reverse()
    return final_list

# testing
str=''
for each_char in decode_string('3[2[ad]3[pf]]xyz'):
    str+=each_char
print(str)