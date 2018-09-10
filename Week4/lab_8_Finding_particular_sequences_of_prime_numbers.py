# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.


# Insert your code here

def check_prime(number):# check whether the number is a prime or not
    # using AKS algorithm
    # integer   ->  bool
    if number==2:
        return True
    if number==3:
        return True
    if number%2==0:
        return False
    if number%3==0:
        return False
    i=5
    w=2
    while i*i<=number:
        if number%i==0:
            return False
        i+=w
        w=6-w
    return True

# def check_prime(number):
#     if number==2:
#         return True
#     if number==3:
#         return True
#     for i in range(2,number):
#         if number%i==0:
#             return False
#     return True

def save_prime(start_number,end_number):
    prime_list=[]
    for i in range(start_number,end_number+1):
        if check_prime(i):
            prime_list.append(i)
    return prime_list

def find_six_consecutive_numbers(prime_list):
    length_of_prime_list=len(prime_list)
    six_consecutive_numbers_list=[]
    for i in range(0,length_of_prime_list-5):
        # if prime_list[i+1]==prime_list[i]+2:
        #     if prime_list[i+2]==prime_list[i+1]+4:
        #         if prime_list[i+3]==prime_list[i+2]+6:
        #             if prime_list[i+4]==prime_list[i+3]+8:
        #                 if prime_list[i+5]==prime_list[i+4]+10:
        #                     six_consecutive_numbers_list.append([prime_list[x] for x in range(i+1,i+6)])
        flag=True
        for t in range(1,6):
            if not prime_list[i+t]==prime_list[i+t-1]+t*2:
                flag=False
        if flag==True:
            six_consecutive_numbers_list.append([prime_list[x] for x in range(i, i + 6)])
    return six_consecutive_numbers_list

def show(six_consecutive_numbers_list):
    print('The solutions are:')
    print()
    for each in six_consecutive_numbers_list:
        for index in range(0,5):
            print(f'{each[index]} ',end='')
        print(f'{each[5]}')
show(find_six_consecutive_numbers(save_prime(10000,99999)))