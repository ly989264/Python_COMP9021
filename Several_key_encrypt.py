# writing a program to encrypt a file with several keys

from string import printable
import sys
import os
import re

available_characters_list=[printable[i] for i in range(0,len(printable)-3)]
available_characters_dict={available_characters_list[i]:i for i in range(0,len(available_characters_list))}
anti_available_characters_dict={i:available_characters_list[i] for i in range(0,len(available_characters_list))}

# print(f'available_characters_list: {available_characters_list}')
# print(f'available_characters_dict: {available_characters_dict}')
# print(f'anti_available_characters_dict: {anti_available_characters_dict}')

def get_keys():
    '''
    :return: a list of several key strings
    '''
    key_string=input('Please input the keys, separated by one and exactly one space:\n')
    key_list=key_string.split(' ')
    for each_key in key_list:
        for each in each_key:
            if each not in available_characters_list:
                print('No available key inputted.')
                sys.exit()
    return key_list

def get_source_filename():
    '''
    get the source filename from the user
    :return: the source filename as a string
    '''
    source_filename=input('Please input the source file name: ')
    path_pattern = re.compile('/(.*?)/(.*)$')
    path_result = re.match(path_pattern, source_filename)
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

def encrypt_or_decrypt(key,source_filename,target_filename,mode):
    if mode==1:# it means that encryption and the source file is the unencrypted file, the target file is the encrypted file
        with open(source_filename,'r') as source:
            with open(target_filename,'w') as target:
                first_current_working=0
                # second_current_working=0
                for each_line in source:
                    temp_list=[]
                    for each_char in each_line:
                        temp_list.append(anti_available_characters_dict[(available_characters_dict[each_char]+available_characters_dict[each_key[first_current_working]])%len(available_characters_list)])
                        first_current_working=(first_current_working+1)%len(each_key)
                        # second_current_working = (second_current_working + 1) % len(second_key)
                    target.write(''.join(temp_list))
    else:
        with open(source_filename,'r') as source:
            with open(target_filename,'w') as target:
                first_current_working = 0
                # second_current_working = 0
                for each_line in source:
                    temp_list=[]
                    for each_char in each_line:
                        temp_list.append(anti_available_characters_dict[(available_characters_dict[each_char]-available_characters_dict[each_key[first_current_working]])%len(available_characters_list)])
                        first_current_working=(first_current_working+1)%len(each_key)
                        # second_current_working = (second_current_working + 1) % len(second_key)
                    target.write(''.join(temp_list))
    return

# testing
mode=input('Do you want to encrypt or unencrypt? ')
pattern_encrypt=re.compile('^en?c?r?y?p?t?',re.I)
if re.match(pattern_encrypt,mode):
    mode=1
else:
    mode=-1
multi_file_mode=input('Do you want to operate on multiple files? ')
pattern_multi_file_mode=re.compile('YE?S?',re.I)
if re.match(pattern_multi_file_mode,multi_file_mode):
    multi_file_mode=1# means that encrypt multi files
else:
    multi_file_mode=-1# means that encrypt single files
if multi_file_mode==-1:
    current_working_path=os.getcwd()
    source_filename=get_source_filename()
    target_filename='temp.py'
    key_list=get_keys()
    if mode==-1:
        key_list.reverse()
    for each_key in key_list:
        encrypt_or_decrypt(each_key,source_filename,target_filename,mode)
        os.remove(source_filename)
        os.rename(target_filename,source_filename)
    print('Done.')
    os.chdir(current_working_path)
else:
    whole_directory_mode=input('Do you want to operate on the whole directory? ')
    if re.match(pattern_multi_file_mode,whole_directory_mode):
        whole_directory_mode=1
    else:
        whole_directory_mod=-1
    if whole_directory_mode==1:# operate on the whole directory
        current_working_path = os.getcwd()
        source_filepath=input('Please input the source file path: (begin with .) ')
        path_pattern = re.compile('^\./.*?$')
        path_result = re.match(path_pattern, source_filepath)
        if not path_result:
            print('Invalid path inputted.')
            sys.exit()
        source_filename_list = os.listdir(source_filepath)
        final_source_filename_list=[]
        for eachelement in source_filename_list:
            if eachelement.startswith('_'):
                pass
            else:
                final_source_filename_list.append(eachelement)
        os.chdir(source_filepath)
        target_filename = 'temp.py'
        key_list = get_keys()
        for source_filename in final_source_filename_list:
            if mode == -1:
                key_list.reverse()
            for each_key in key_list:
                encrypt_or_decrypt(each_key, source_filename, target_filename, mode)
                os.remove(source_filename)
                os.rename(target_filename, source_filename)
        print('Done.')
        os.chdir(current_working_path)
    else:
        current_working_path = os.getcwd()
        print('You are using the multiple files mode! ')
        source_filepath = input('Please input the source filepath: (begin with .) ')
        path_pattern = re.compile('^\./.*?$')
        path_result = re.match(path_pattern, source_filepath)
        if not path_result:
            print('Invalid path inputted.')
            sys.exit()
        filename_string=input('Please input the filenames, separated by one space character:\n')
        final_source_filename_list=filename_string.split(' ')
        os.chdir(source_filepath)
        target_filename = 'temp.py'
        key_list = get_keys()
        for source_filename in final_source_filename_list:
            if mode == -1:
                key_list.reverse()
            for each_key in key_list:
                encrypt_or_decrypt(each_key, source_filename, target_filename, mode)
                os.remove(source_filename)
                os.rename(target_filename, source_filename)
        print('Done.')
        os.chdir(current_working_path)