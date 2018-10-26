# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# Given "25525511135", return
#
# [
#   "255.255.11.135",
#   "255.255.111.35"
# ]

def restore_possible_id_address(string,stage,list):
    global final_list
    if stage==4 and len(string)==0:
        final_list.append(list)
        return
    for length in range(1,4):
        if len(string)<length:
            continue
        else:
            new_string=string[length:]
            temp=[]
            num=int(string[0:length])
            if num>255:
                continue
            for each_element in list:
                temp.append(each_element)
            temp.append(string[0:length])
            restore_possible_id_address(new_string,stage+1,temp)
    return

final_list=[]
restore_possible_id_address('22522511135',0,[])
for each in final_list:
    print(each)
print(len(final_list))