from self_stack import *
import re

def calcualte_postfix_string(string): # no parentheses in the string
    '''
    :param string: e.g. '2 3 + 5 *'
    :return: the calculation value
    '''
    operator_library={
        '+':lambda x,y:x+y,
        '-':lambda x,y:y-x,
        '*':lambda x,y:x*y,
        '/':lambda x,y:y/x,
        '//': lambda x,y:y//x,
        '%':lambda x,y:y%x
    }
    string=string.strip()
    string=re.sub(' +',' ',string)
    op_list=string.split(' ')
    stack=Stack()
    while op_list:
        current_char=op_list.pop(0)
        if current_char in operator_library.keys():
            temp1=stack.pop()
            temp2=stack.pop()
            stack.push(operator_library[current_char](temp1,temp2))
            # print(f'{current_char},{temp1},{temp2}')
        else:
            current_char=int(current_char)
            stack.push(current_char)
    if len(stack)!=1:
        print('Length of the stack is not 1.')
    return stack.pop()

def calcualte_infix_string(string): # include the parentheses and others
                                    # spaces needed
    separator_library={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    operator_library = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y / x,
        '//': lambda x, y: y // x,
        '%': lambda x, y: y % x
    }
    string=string.strip()
    string=re.sub(' +',' ',string)
    op_list=string.split(' ')
    # print(op_list)
    stack=Stack()
    while op_list:
        current_char=op_list.pop(0)
        # print(current_char)
        if current_char in separator_library.keys():
            target_char=separator_library[current_char]
            temp_list=[]
            operator=None
            while stack.peek() != target_char:
                temp=stack.pop()
                if temp in operator_library.keys():
                    operator=temp
                else:
                    temp_list.append(temp)
            stack.pop()
            stack.push(operator_library[operator](temp_list[0],temp_list[-1]))
            # print(f'{operator},{temp_list}')
        else:
            try:
                stack.push(int(current_char))
            except:
                stack.push(current_char)
    if len(stack)>1:
        temp_list = []
        operator = None
        while not stack.is_empty():
            temp = stack.pop()
            if temp in operator_library.keys():
                operator = temp
            else:
                temp_list.append(temp)
        return operator_library[operator](temp_list[0],temp_list[-1])
    elif stack.is_empty():
        return 0
    else:
        return stack.pop()

def calcualte_infix_string_without_spaces(string):
    number_list=[str(i) for i in range(0,10)]
    new_string=''
    for each_char_index in range(len(string)-1):
        if string[each_char_index] in number_list and string[each_char_index+1] in number_list:
            new_string+=string[each_char_index]
        elif string[each_char_index]=='/' and string[each_char_index+1]=='/':
            new_string+=string[each_char_index]
        else:
            new_string+=string[each_char_index]
            new_string+=' '
    new_string+=string[-1]
    return calcualte_infix_string(new_string)


# TESTING
# string=' 12   13 4 5 + + 10 -  7 8 * / +'
# print(calcualte_postfix_string(string))
# string='[ ( { 2 // 1 } + 5 )  * ( 5 - 3 ) ] * 3'
# print(calcualte_infix_string(string))
string= '[({2//1}+5)*(5-3)]*3'
print(calcualte_infix_string_without_spaces(string))