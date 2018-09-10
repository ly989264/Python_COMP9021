import os

def convert(char,number):
    temp_number=ord(char)
    new_number=(temp_number+number)%128
    return chr(new_number)

# testing
# string='fjjJJKJ *jfj-=!'
# for each in string:
#     print(convert(convert(each,60),-60),end='')
# print()

def ad(filename1,number):# ord() chr()
    if not os.path.exists(filename1):
        return None
    filename2='temp__fil.py'
    with open(filename1,'r') as f1:
        with open(filename2,'w') as f2:
            for eachline in f1:
                for item in eachline:
                    f2.write(convert(item,number))
    os.remove(filename1)
    os.rename(filename2,filename1)
