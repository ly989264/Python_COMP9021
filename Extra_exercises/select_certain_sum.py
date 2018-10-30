
def select_certain_sum(list,sum,result):
    global final_list
    if sum==0:
        result.sort()
        if result not in final_list:
            final_list.append(result)
        return
    if sum<0:
        return
    if not list:
        return
    already_list=[]
    for each_element_index in range(len(list)):
        each_element=list[each_element_index]
        if each_element not in already_list:
            already_list.append(each_element)
            temp=result[:]
            temp.append(each_element)
            select_certain_sum(list[0:each_element_index]+list[each_element_index+1:],sum-each_element,temp)
    return

final_list=[]
select_certain_sum([1,1,1,2,5,8,2,6,7,9,5,6,1,2,1,1,1,2,1,2,4,2,1,5,1,3,9,7,5,6,0,3,5,2,3,4],15,[])
print(len(final_list))