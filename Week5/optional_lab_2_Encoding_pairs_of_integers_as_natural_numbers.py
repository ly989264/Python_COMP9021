from math import sqrt


def encode(a, b):
    '''
    encode (a,b) to the integer value
    :param a: x
    :param b: y
    :return: integer that in the position of (a,b)
    '''
    outsider=1
    current_outsider=1
    insider=1# if insider==2, then add the outsider
    state=0# right
    current_x=0
    current_y=0
    result=0
    while not (current_x==a and current_y==b):
        result+=1
        if state==0:# add x
            current_x+=1
        elif state==1:# add y
            current_y+=1
        elif state==2:# minus x
            current_x-=1
        elif state==3:# minus y
            current_y-=1
        #print(current_x,current_y)
        if current_outsider==outsider:
            if insider==2:
                insider=1
                outsider+=1
            else:
                insider+=1
            current_outsider=1
            if state==3:
                state=0
            else:
                state+=1
        else:
            current_outsider+=1
        #print(outsider,current_outsider,insider,state)
    return result

def decode(n):
    '''
    decode the integer to the (a,b) format
    :param n: integer
    :return: (a,b) format
    '''
    outsider = 1
    current_outsider = 1
    insider = 1  # if insider==2, then add the outsider
    state = 0  # right
    current_x = 0
    current_y = 0
    number=0
    while number<n:
        number += 1
        if state == 0:  # add x
            current_x += 1
        elif state == 1:  # add y
            current_y += 1
        elif state == 2:  # minus x
            current_x -= 1
        elif state == 3:  # minus y
            current_y -= 1
        if current_outsider == outsider:
            if insider == 2:
                insider = 1
                outsider += 1
            else:
                insider += 1
            current_outsider = 1
            if state == 3:
                state = 0
            else:
                state += 1
        else:
            current_outsider += 1
    return current_x,current_y
