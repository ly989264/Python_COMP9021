# Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.
# Given [1,2,[1,2]], return [1,2,1,2]
# Given [4,[3,[2,[1]]]], return [4,3,2,1]

def flatten_list(List,temp):
    global final_list
    if not len(List):
        final_list.append(temp)
        return
    if isinstance(List[0],int):
        temp.append(List[0])
        flatten_list(List[1:],temp)
    elif isinstance(List[0],list):
        new_list=[]
        for each_element in List[0]:
            new_list.append(each_element)
        List.pop(0)
        new_list+=List
        temp.append(new_list.pop(0))
        flatten_list(new_list,temp)
    return

final_list=[]
flatten_list([4,[3,[2,[1]]]],[])
print(final_list)