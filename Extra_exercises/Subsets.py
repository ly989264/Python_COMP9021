# Given a set of distinct integers, return all possible subsets.

def operate(final_list,list,part_of_result):
    part_of_result.sort()
    if part_of_result not in final_list:
        final_list.append(part_of_result)
    if len(list)==0:
        return
    for index in range(len(list)):
        temp=[]
        for each_element in part_of_result:
            temp.append(each_element)
        temp.append(list[index])
        operate(final_list,list[0:index]+list[index+1:],temp)
    return

def get_subset(list):
    final_list=[[]]
    length_of_list=len(list)
    for index in range(len(list)):
        operate(final_list,list[0:index]+list[index+1:],[list[index]])
    return final_list

# testing
List=[1,2,2,3,1,4,5,6]
final_list=get_subset(List)
final_list.sort(key=lambda x:len(x))
for each in final_list:
    print(each)