# During the NBA playoffs, we always arrange the rather strong team to play with the rather weak team, like make the rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting. Now, you're given n teams, you need to output their final contest matches in the form of a string.
#
# The n teams are given in the form of positive integers from 1 to n, which represents their initial rank. (Rank 1 is the strongest team and Rank n is the weakest team.) We'll use parentheses('(', ')') and commas(',') to represent the contest team pairing - parentheses('(' , ')') for pairing and commas(',') for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.
import sys

def generate_matching_pairs(current_list):
    if len(current_list)==0:
        print('The list is empty.')
        sys.exit()
    if len(current_list)==1:
        global final_list
        final_list.append(current_list)
        return
    temp_new_list=[]
    for each_first_part_index in range(len(current_list)//2):
        new_pair=(current_list[each_first_part_index],current_list[len(current_list)-each_first_part_index-1])
        temp_new_list.append(new_pair)
    generate_matching_pairs(temp_new_list)
    return


final_list=[]
generate_matching_pairs([i for i in range(1,9)])
print(final_list)