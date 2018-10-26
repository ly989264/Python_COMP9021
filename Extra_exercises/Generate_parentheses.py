# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"

def generate_parentheses(first_list,second_list,string):
    global final_list
    if len(first_list)==0 and len(second_list)==0:
        final_list.append(string)
        return
    if len(first_list)>len(second_list):
        return
    if len(first_list)==len(second_list):
        temp=''
        for each_char in string:
            temp+=each_char
        temp+=first_list[0]
        generate_parentheses(first_list[1:],second_list,temp)
        return
    elif len(first_list)<len(second_list) and len(first_list)!=0:
        temp=''
        for each_char in string:
            temp+=each_char
        temp+=second_list[0]
        generate_parentheses(first_list,second_list[1:],temp)
        temp=''
        for each_char in string:
            temp+=each_char
        temp+=first_list[0]
        generate_parentheses(first_list[1:],second_list,temp)
        return
    elif len(first_list)<len(second_list) and len(first_list)==0:
        for each_element in second_list:
            string+=each_element
        final_list.append(string)
        return


n=10
first_list=['(' for _ in range(n)]
second_list=[')' for _ in range(n)]
final_list=[]
generate_parentheses(first_list,second_list,'')
print(final_list)