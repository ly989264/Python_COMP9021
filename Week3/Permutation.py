# Given a list of numbers, return all possible permutations.
# For nums = [1,2,3], the permutations are:
#
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
# using random list to solve this problem
from random import randrange

def get_and_resort(list):
    length=len(list)
    copy_list=list[:]
    new_list=[]
    while len(copy_list):
        random_index=randrange(0,length)
        new_list.append(copy_list[random_index])
        copy_list.pop(random_index)
        length-=1
    return new_list

nums=[1,3,4,5,6,9,8]
result_list=[]
length_of_nums=len(nums)
expect_length=1
for each in range(length_of_nums,1,-1):
    expect_length*=each
for i in range(0,1000000):
    new_list=get_and_resort(nums)
    if new_list in result_list:
        continue
    else:
        result_list.append(new_list)
    if len(result_list)>=expect_length:
        break
print(result_list)
