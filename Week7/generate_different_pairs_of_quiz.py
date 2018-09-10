# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by *** and Eric Martin for COMP9021
from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()


def save_1s_coordinate(grid):
    full_list=[]
    for i in range(0,dim):
        for j in range(0,dim):
            if grid[i][j]:
                full_list.append((i,j))
    return full_list

def calculate_eight_coordinate(x,y):
    a=1
    b=2
    return [(x+a,y+b),(x+b,y+a),(x+b,y-a),(x+a,y-b),(x-a,y+b),(x-b,y+a),(x-b,y-a),(x-a,y-b)]

def check_full_list_element_in_result_list(full_list,result_list):
    existing_element_list=[]
    for eachelement in result_list:
        if eachelement in full_list:
            existing_element_list.append(eachelement)
    return existing_element_list

def explore_board():
    full_list=save_1s_coordinate(grid)
    class_list=[]
    # print('full_list: ',full_list)
    while full_list:
        # print('Before this full list: ',full_list)
        temp_already_list=[]
        first_deal=full_list.pop(0)
        result_list=calculate_eight_coordinate(*first_deal)
        existing_element_list=check_full_list_element_in_result_list(full_list,result_list)
        temp_already_list.append(first_deal)
        while existing_element_list:
            # print(existing_element_list)
            to_deal_element=existing_element_list.pop(0)
            # for index in range(0,len(existing_element_list)):
            #     if existing_element_list[index] not in temp_already_list:
            #         to_deal_element=existing_element_list.pop(index)
            temp_already_list.append(to_deal_element)
            new_result_list=calculate_eight_coordinate(*to_deal_element)
            new_existing_element_list=check_full_list_element_in_result_list(full_list,new_result_list)
            for each in new_existing_element_list:
                if each not in temp_already_list:
                    if each not in existing_element_list:
                        existing_element_list.append(each)
            for each in existing_element_list:
                if each in temp_already_list:
                    existing_element_list.remove(each)
        # print('temp_already_list: ',temp_already_list)
        # print('Current_full_list: ',full_list)
        for each in temp_already_list:
            if each in full_list:
                full_list.remove(each)
        class_list.append(temp_already_list)
        # print(temp_already_list)
    return len(class_list)

with open('q_6_result.txt','w') as w:
    for for_seed in range(0,20):
        for n in range(-100,101):
            if not n:
                continue
            seed(for_seed)
            if n > 0:
                grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
            else:
                grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]

            # testing
            # display_grid()
            # print(len(save_1s_coordinate(grid)))
            # print(explore_board())
            print(f'for_seed={for_seed},n={n},result={explore_board()}',file=w)
            # print('Here is the grid that has been generated:')
            # display_grid()
            # nb_of_knights = explore_board()
            # if not nb_of_knights:
            #     print('No chess knight has explored this board.')
            # elif nb_of_knights == 1:
            #     print(f'At least 1 chess knight has explored this board.')
            # else:
            #     print(f'At least {nb_of_knights} chess knights have explored this board')
