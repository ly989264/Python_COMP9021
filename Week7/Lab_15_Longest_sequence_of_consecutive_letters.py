# Prompts the user for a string w of lowercase letters and outputs the
# longest sequence of consecutive letters that occur in w,
# but with possibly other letters in between, starting as close
# as possible to the beginning of w.


import sys


# Insert your code here
inputted_string=input('Please input a string of lowercase letters: ')
result_list=[]
for eachletter in inputted_string:
    if eachletter=='a':
        if len(result_list):
            continue
        else:
            result_list.append([eachletter])
    else:
        eachletter_before=chr(ord(eachletter)-1)
        flag=True
        if not len(result_list):
            result_list.append([eachletter])
        else:
            for each_sublist in result_list:
                if eachletter_before in each_sublist:
                    if eachletter in each_sublist:
                        pass
                    else:
                        each_sublist.append(eachletter)
                    flag=False
                    break
            if flag:
                result_list.append([eachletter])
max_length=0
max_list=[]
for item in result_list:
    current_length=len(item)
    if current_length>max_length:
        max_length=current_length
        max_list=item[:]
max_string=''.join(max_list)
print(f'The solution is: {max_string}')
