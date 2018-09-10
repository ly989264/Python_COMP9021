import sys
sys.path.append('C:/Users')
import ad
import os
filename=input('The filename: ')
filename=filename.lower()
file_list=os.listdir(os.getcwd())
flag=False
for each in file_list:
    each=each.lower()
    if each.startswith(filename):
        filename=each
        flag=True
        break
if not flag:
    print(f'Cannot find the {filename}.')
    sys.exit()
number=int(input('The number: '))
ad.ad(filename,number)