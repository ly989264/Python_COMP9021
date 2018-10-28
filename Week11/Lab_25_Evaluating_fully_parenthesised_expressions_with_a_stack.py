'''
Uses the Stack interface to evaluate an arithmetic expression written in postfix
and built from natural numbers using the binary +, -, * and / operators.
'''


import re
from operator import add, sub, mul, truediv

from stack_adt import Stack, EmptyStackError


# def evaluate(expression):
#     '''
#     Checks whether an expression is a valid postfix expression,
#     and in case the answer is yes, returns the value of the expression,
#     provided that no division by 0 is attempted; otherwise, return None.
#
#     >>> evaluate('12')
#     12
#     >>> evaluate('12 345 +')
#     357
#     >>> evaluate('1 2 3 4 5 6 + - + - +')
#     7
#     >>> evaluate('10 2 * 30 4 * -')
#     -100
#     >>> evaluate('12 13 4 5+ + 10 -  7 8 * /+')
#     12.214285714285714
#     >>> evaluate('2 +')
#     >>> evaluate('2 3')
#     >>> evaluate('2 / 3')
#     >>> evaluate('2 0 /')
#     '''
#     if any(not (c.isdigit() or c.isspace() or c in '+-*/') for c in expression):
#         return
#     # Tokens can be natural numbers, +, -, *, and /
#     tokens = re.compile('(\d+|\+|-|\*|/)').findall(expression)
#     # print(tokens)
#     try:
#         value = evaluate_expression(tokens)
#         return value
#     except ZeroDivisionError:
#         return
#
# def evaluate_expression(tokens):
#     stack = Stack()
#     for token in tokens:
#         try:
#             token = int(token)
#             stack.push(token)
#         except ValueError:
#             try:
#                 arg_2 = stack.pop()
#                 arg_1 = stack.pop()
#                 stack.push({'+': add, '-': sub, '*': mul, '/': truediv}[token](arg_1, arg_2))
#             except EmptyStackError:
#                 return
#     if stack.is_empty():
#         return
#     value = stack.pop()
#     if not stack.is_empty():
#         return
#     return value

def calcualte_infix_string(string):  # include the parentheses and others and spaces needed
    separator_library = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    operator_library = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y / x,
        '//': lambda x, y: y // x,
        '%': lambda x, y: y % x
    }
    string = string.strip()
    string = re.sub(' +', ' ', string)
    op_list = string.split(' ')
    # cp_list=op_list[:]
    # print(op_list)
    stack = Stack()
    # flag=False
    while op_list:
        # flag=True
        current_char = op_list.pop(0)
        # print(current_char)
        if current_char in separator_library.keys():
            target_char = separator_library[current_char]
            temp_list = []
            operator = None
            count=0
            while stack.peek() != target_char:
                temp = stack.pop()
                if temp in operator_library.keys():
                    operator = temp
                    count+=1
                else:
                    temp_list.append(temp)
            if count>1 or count==0:
                return None
            if len(temp_list)>2:
                return None
            stack.pop()
            if operator == '-' and len(temp_list) == 1:
                stack.push(temp_list[0]*-1)
            elif (operator == '/' or operator=='//') and temp_list[0]==0:
                    return None
            else:
                stack.push(operator_library[operator](temp_list[0], temp_list[-1]))
            # print(f'{operator},{temp_list}')
        else:
            try:
                stack.push(int(current_char))
            except:
                stack.push(current_char)
    # reflag=False
    # if flag:
    #     for each in string:
    #         if each in separator_library.keys():
    #             reflag=True
    #             break
    # if not reflag:
    #     if len(cp_list)>1:
    #         return None
    if len(stack) > 1:
        temp_list = []
        operator = None
        count=0
        while not stack.is_empty():
            temp = stack.pop()
            if temp in operator_library.keys():
                operator = temp
                count+=1
            else:
                temp_list.append(temp)
        if count>1 or count==0:
            return None
        if len(temp_list)>2:
            return None
        if operator is not None:
            return None
        else:
            return temp_list[0]
        # if operator == '-' and len(temp_list) == 1:
        #     return temp_list[0] * -1
        # elif (operator == '/' or operator == '//') and temp_list[0] == 0:
        #         return None
        # else:
        #     return operator_library[operator](temp_list[0], temp_list[-1])
    elif stack.is_empty():
        return 0
    else:
        return stack.pop()


def evaluate(string):
    number_list = [str(i) for i in range(0, 10)]
    new_string = ''
    for each_char_index in range(len(string) - 1):
        if string[each_char_index] in number_list and string[each_char_index + 1] in number_list:
            new_string += string[each_char_index]
        elif string[each_char_index] == '/' and string[each_char_index + 1] == '/':
            new_string += string[each_char_index]
        else:
            new_string += string[each_char_index]
            new_string += ' '
    new_string += string[-1]
    return calcualte_infix_string(new_string)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
# print(evaluate('[1-{20+300}]'))
# print(evaluate('[(1-20)+300]'))
# print(evaluate('(100 + (-50))'))
# print(evaluate('({20*4}/5)'))
# print(evaluate('100+3'))