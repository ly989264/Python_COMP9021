# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10)
# Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4 * 2 + 6 * 3 = 27)


def calculate_weight_sum(l,level):
    global total_sum
    if not l:
        return
    if not isinstance(l,list):
        # print(f'{l}*{level}')
        total_sum+=l*level
        return
    else:
        for each_element in l:
            calculate_weight_sum(each_element,level+1)
    return

total_sum=0
calculate_weight_sum([[1,1],2,[1,1]],0)
print(total_sum)
total_sum=0
calculate_weight_sum([1,[4,[6]]],0)
print(total_sum)