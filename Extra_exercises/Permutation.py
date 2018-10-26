# Given a list of numbers, return all possible permutations.


def operate(final_list,nums,list):
    if len(nums)==0:
        final_list.append(list)
        return
    for each_index in range(len(nums)):
        temp=[]
        for each in list:
            temp.append(each)
        temp.append(nums[each_index])
        operate(final_list,nums[0:each_index]+nums[each_index+1:],temp)
    return

def permute(nums):
    '''
    :param nums: a list of integers
    :return: a list of permutations
    '''
    final_list=[]
    for each_index in range(len(nums)):
        operate(final_list,nums[0:each_index]+nums[each_index+1:],[nums[each_index]])
    already_list=[]
    result_list=[]
    for each_element in final_list:
        if each_element not in already_list:
            already_list.append(each_element)
            result_list.append(each_element)
    return result_list

# testing
print(permute([1,2,3]))

