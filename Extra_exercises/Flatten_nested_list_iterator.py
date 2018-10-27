# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
# Given the list [[1,1],2,[1,1]], By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
#
# Given the list [1,[4,[6]]], By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

# [1,[[2,3],4,[5,[6,7]]]] -> [1,2,3,4,5,6,7]

import sys
import re

def flatten_nested_list(flatten_list):
    global final_list
    if not flatten_list:
        return
    if not isinstance(flatten_list,list):
        final_list.append(flatten_list)
        return
    flatten_nested_list(flatten_list[0])
    flatten_nested_list(flatten_list[1:])
    return

final_list=[]
flatten_nested_list([1,[[2,3],4,[5,[6,7]]]])
print(final_list)
final_list=[]
flatten_nested_list([1,[4,[6]]])
print(final_list)
final_list=[]
flatten_nested_list([[1,1],2,[1,1]])
print(final_list)