
'''
Given strictly positive integers N and D, outputs N / D in the form
                 1 / d_1 + ... + 1 / d_k
if N < D, and in the form
                 p + 1 / d_1 + ... + 1 /d_k
if N >= D,
- for one function, applying Fibonacci's method (which yields a unique decomposition),
- for another function, determining all decompositions of minimal length (which might yield
  many decompositions).
'''

# WORKS BUT CANNOT RUN EFFICIENTLY

from math import gcd


# Possibly define other functions

def get_cd(number):
    cd_list=[]
    for i in range(1,number+1):
        if not number%i:
            cd_list.append(i)
    return cd_list

def select_couples_from_list(list,sum):
    if not list:
        if sum==0:
            return [[]]
        else:
            return []
    return select_couples_from_list(list[1:], sum) + \
           [[list[0]] + tail for tail in
            select_couples_from_list(list[1:], sum - list[0])]

def fibonacci_decomposition(N, D):
    integer_num=0
    print(f'{N}/{D} = ',end='')
    if N>D:
        integer_num=N//D
        N=N%D
    elif N==D:
        integer_num=1
        N=0
    if N==0:
        print(f'{integer_num}')
    else:
        current_gcd = gcd(N, D)
        if current_gcd != 1:
            N=N//current_gcd
            D=D//current_gcd
        while N!=1:
            d1=D//N+1
            print(f'1/{d1} + ',end='')
            N=N*d1-D
            D=D*d1
            current_gcd = gcd(N, D)
            if current_gcd != 1:
                N = N // current_gcd
                D = D // current_gcd
        print(f'1/{D}')

def key(x):
    return len(x),x

def shortest_length_decompositions(N, D):
    original_N=N
    original_D=D
    # fib
    integer_num = 0
    if N > D:
        integer_num = N // D
        N = N % D
    elif N == D:
        integer_num = 1
        N = 0
    if N == 0:
        pass
    else:
        current_gcd = gcd(N, D)
        if current_gcd != 1:
            N = N // current_gcd
            D = D // current_gcd
        while N != 1:
            d1 = D // N + 1
            N = N * d1 - D
            D = D * d1
            current_gcd = gcd(N, D)
            if current_gcd != 1:
                N = N // current_gcd
                D = D // current_gcd
        final=D
    max_multi=final//original_D
    final_list=[]
    for each_multi in range(1,max_multi+1):
        current_max=each_multi*original_D
        cd_list=get_cd(current_max)
        target_sum=original_N*each_multi
        current_list=select_couples_from_list(cd_list,target_sum)
        for each_list in current_list:
            temp_list=[]
            for each_element in each_list:
                temp_list.append(int(current_max/each_element))
            temp_list.sort()
            final_list.append(temp_list)
    final_list.sort(key=key)
    shortest_length=len(final_list[0])
    already_list=[]
    for each_list in final_list:
        if each_list in already_list:
            continue
        if len(each_list)==shortest_length:
            print(f'{original_N}/{original_D} = ',end='')
            for each_element_index in range(shortest_length-1):
                print(f'1/{each_list[each_element_index]} + ',end='')
            print(f'1/{each_list[-1]}')
            already_list.append(each_list)
        else:
            break

shortest_length_decompositions(4,17)