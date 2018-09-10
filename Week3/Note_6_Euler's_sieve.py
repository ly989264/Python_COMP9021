# using Euler's sieve to find all primes smaller and equals to certain number

from math import sqrt
from timeit import timeit

def get_prime_list(number):
    sieve_list=[True]*(number+1)
    for outer in range(2,round(sqrt(number))+1):
        if not sieve_list[outer]:
            continue
        else:
            mul_index=outer
            while outer*mul_index<=number:
                zs=1
                while outer**zs*mul_index<=number:
                    index=outer**zs*mul_index
                    sieve_list[index]=False
                    zs+=1
                for x in range(mul_index+1,len(sieve_list)):
                    if sieve_list[x]:
                        mul_index=x
                        break
    largest_element=len(sieve_list)-1
    while not sieve_list[largest_element]:
        largest_element-=1
    return ((i for i in range(2,len(sieve_list)) if sieve_list[i]),len(str(largest_element)))

def get_prime_list_version_two(number):
    sieve=list(range(2,number+1))
    i=0
    while sieve[i]<=round(sqrt(number)):# using while rather than for because the list is always changing
        upper=1
        while sieve[i]**upper<=number:
            k=0
            second_multi=sieve[i+k]
            while sieve[i]**upper*second_multi<=number:
                if sieve[i]**upper*second_multi in sieve:# meet a problem that does not exist in version three
                    sieve.remove(sieve[i] ** upper * second_multi)
                k+=1
                second_multi = sieve[i + k]
            upper+=1
        i+=1
    largest_element=sieve[-1]
    return sieve,len(str(largest_element))

def get_prime_list_version_three(number):
    sieve=list(range(2,number+1))
    i=0
    while sieve[i]<=round(sqrt(number)):# using while rather than for because the list is always changing
        k=0
        while True:
            factor=sieve[i]*sieve[i+k]
            if factor>number:
                break
            while factor<=number:
                sieve.remove(factor)
                factor*=sieve[i]
            k+=1
        i+=1
    return sieve,len(str(sieve[-1]))

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

#display(*(get_prime_list_version_two(20000)))
print(timeit('get_prime_list_version_two(200000)','from __main__ import get_prime_list_version_two',number=1))