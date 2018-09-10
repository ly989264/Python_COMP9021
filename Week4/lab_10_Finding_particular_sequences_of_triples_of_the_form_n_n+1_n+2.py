# Finds all triples of consecutive positive three-digit integers
# each of which is the sum of two squares.


# Insert you code here
from math import sqrt

def check_and_get(integer):# given an integer, check whether it is the sum of squares, if so, also get the a and b
    certain_1=sqrt(integer)
    certain_1_int=int(certain_1)
    certain_2=sqrt(integer/2)
    certain_2_int=int(certain_2)
    for a in range(certain_2_int,-1,-1):
        for b in range(certain_1_int,certain_2_int-1,-1):
            if a*a+b*b==integer:
                return a,b
    return None,None

def walk_through():
    index_list=[i for i in range(100,1000)]
    ab_tuple_list=[]
    for each_item in index_list:
        ab_tuple=check_and_get(each_item)
        ab_tuple_list.append(ab_tuple)
        if ab_tuple[0]!=None and each_item>=102:
            if ab_tuple_list[each_item-102][0]!=None and ab_tuple_list[each_item-101][0]!=None:
                print(f'({each_item-2}, {each_item-1}, {each_item}) '
                      f'(equal to ({ab_tuple_list[each_item-102][0]}^2+{ab_tuple_list[each_item-102][1]}^2, '
                      f'{ab_tuple_list[each_item-101][0]}^2+{ab_tuple_list[each_item-101][1]}^2, '
                      f'{ab_tuple[0]}^2+{ab_tuple[1]}^2)) '
                      f'is a solution.')
walk_through()
