# writing a program to encrypt a file with two keys, with first_key[0]*second_key[0]

from string import printable
import sys
import os
import re

available_characters_list=[printable[i] for i in range(0,len(printable)-3)]
available_characters_dict={available_characters_list[i]:i for i in range(0,len(available_characters_list))}
anti_available_characters_dict={i:available_characters_list[i] for i in range(0,len(available_characters_list))}

def get_keys():
    '''
    get two strings as keys from the user and return them as a tuple
    :return: a tuple of two key strings
    '''
    first_key=input('Please input the first key: ')
    for each in first_key:
        if each not in available_characters_list:
            print('No available key inputted.')
            sys.exit()
    second_key = input('Please input the second key: ')
    for each in second_key:
        if each not in available_characters_list:
            print('No available key inputted.')
            sys.exit()
    return first_key,second_key

def get_source_filename():
    '''
    get the source filename from the user
    :return: the source filename as a string
    '''
    source_filename=input('Please input the source file name: ')
    path_pattern = re.compile('/(.*?)/(.*$)')
    path_result = re.search(path_pattern, source_filename)
    if path_result:
        new_working_path = path_result.group(1)
        source_filename = path_result.group(2)
    else:
        new_working_path = current_working_path
    os.chdir(new_working_path)
    if not os.path.exists(source_filename):
        print(f'{source_filename} does not exist.')
        sys.exit()
    return source_filename

def get_target_filename():
    '''
    get the target filename from the user
    :return: the target filename as a string
    '''
    target_filename=input('Please input the target file name: ')
    return target_filename

def encrypt_or_decrypt(first_key,second_key,source_filename,target_filename,mode):
    if mode==1:# it means that encryption and the source file is the unencrypted file, the target file is the encrypted file
        with open(source_filename,'r') as source:
            with open(target_filename,'w') as target:
                first_current_working=0
                second_current_working=0
                for each_line in source:
                    temp_list=[]
                    for each_char in each_line:
                        temp_list.append(anti_available_characters_dict[(available_characters_dict[each_char]+available_characters_dict[first_key[first_current_working]]*available_characters_dict[second_key[second_current_working]])%len(available_characters_list)])
                        first_current_working=(first_current_working+1)%len(first_key)
                        second_current_working = (second_current_working + 1) % len(second_key)
                    target.write(''.join(temp_list))
    else:
        with open(source_filename,'r') as source:
            with open(target_filename,'w') as target:
                first_current_working = 0
                second_current_working = 0
                for each_line in source:
                    temp_list=[]
                    for each_char in each_line:
                        temp_list.append(anti_available_characters_dict[(available_characters_dict[each_char]-available_characters_dict[first_key[first_current_working]]*available_characters_dict[second_key[second_current_working]])%len(available_characters_list)])
                        first_current_working=(first_current_working+1)%len(first_key)
                        second_current_working = (second_current_working + 1) % len(second_key)
                    target.write(''.join(temp_list))
    return

# testing
mode=input('Do you want to encrypt or unencrypt? ')
pattern_encrypt=re.compile('^en?c?r?y?p?t?',re.I)
if re.match(pattern_encrypt,mode):
    mode=1
else:
    mode=-1
current_working_path=os.getcwd()
source_filename=get_source_filename()
target_filename='temp.py'
first_key,second_key=get_keys()
encrypt_or_decrypt(first_key,second_key,source_filename,target_filename,mode)
os.remove(source_filename)
os.rename(target_filename,source_filename)
print('Done.')
os.chdir(current_working_path)