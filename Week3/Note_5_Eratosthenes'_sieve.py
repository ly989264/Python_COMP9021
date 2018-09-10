from math import sqrt
from timeit import timeit

def get_prime_list(number):
    sieve_list=[True]*(number+1)
    for i in range(2,round(sqrt(number))):
        if sieve_list[i]:
            for each in range(i*i,number+1,i):
                sieve_list[each]=False
    largest_prime=len(sieve_list)-1
    while not largest_prime:
        largest_prime-=1
    return ((i for i in range(2,len(sieve_list)) if sieve_list[i]),len(str(largest_prime)))

def display(sieve,maxlength):
    width=maxlength+2
    nb_of_eachline=80//width
    count=0
    for each in sieve:
        print(f'{each:{width}}',end='')
        count+=1
        if count==nb_of_eachline:
            print()
            count=0
print(timeit('get_prime_list(2000000)','from __main__ import get_prime_list',number=1))
