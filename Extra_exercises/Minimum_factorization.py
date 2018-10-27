# Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.
#
# If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.
#
# Given a = 48, return 68.
# Given a = 15, return 35.

from math import sqrt

def calculate_mul(n):
    string=str(n)
    result=1
    for each_char in string:
        result*=int(each_char)
    return result

def find_minimum_number_v1(n):
    for i in range(0,n**2):
        if calculate_mul(i)==n:
            return i

def check_prime(n):
    for i in range(2,int(sqrt(n))+1):
        if not n%i:
            return False
    return True

def get_primes(n):
    global prime_list
    if check_prime(n):
        prime_list.append(n)
        return
    for i in range(2,int(sqrt(n))+1):
        if not n%i:
            n=n//i
            prime_list.append(i)
            get_primes(n)
            return
    return

def generate_minumum_number(base_list):
    global final_list
    flag=False
    for each_index in range(len(base_list)):
        for j in range(each_index+1,len(base_list)):
            if base_list[each_index]*base_list[j]<10:
                generate_minumum_number(base_list[0:each_index]+[base_list[each_index]*base_list[j]]+base_list[each_index+1:j]+base_list[j+1:])
                flag=True
    if not flag:
        final_list.append(base_list)

def remove_duplicate(final_list):
    already_list=[]
    new_list=[]
    for each in final_list:
        if each not in already_list:
            already_list.append(each)
            new_list.append(each)
        else:
            continue
    return new_list

# testing
final_list=[]
prime_list=[]
get_primes(48)
prime_list.sort()
generate_minumum_number(prime_list)
new_list=remove_duplicate(final_list)
del final_list
final_list=new_list[:]
final_list.sort(key=lambda x:len(x))
number_list=[]
for each in final_list:
    temp=''.join(str(i) for i in each)
    number_list.append(temp)
current_small=int(number_list[0])
for each in number_list:
     if int(each)<current_small:
         current_small=int(each)
print(current_small)