# Decodes all multiplications of the form
#
#                     ?  *  *  *    number_list1
#                   x ?  ?  *  *    number_list2
#                     ----------
#                     *  *  *  *    result_list1
#                     *  *  *  ?    result_list2
#                     ----------
#                     *  *  *  *    result_list3
#
# such that the sum of all digits in all 4 columns is constant.


# Insert your code here.
# Method 2
def check(number1,number2):
    number2_2,number2_1=divmod(number2,10)
    first_multiply=number2_1*number1
    second_multiply=number2_2*number1
    number_list1=[int(i) for i in str(number1)]
    number_list1.reverse()
    number_list1.append(0)
    number_list2=[int(i) for i in str(number2)]
    number_list2.reverse()
    number_list2.append(0)
    number_list2.append(0)
    result_list1=[int(i) for i in str(first_multiply)]
    result_list1.reverse()
    while len(result_list1)<4:# while! rather than if!
        result_list1.append(0)
    result_list2=[int(i) for i in str(second_multiply)]
    result_list2.append(0)
    result_list2.reverse()
    while len(result_list2)<4:# while! rather than if!
        result_list2.append(0)
    if len(result_list2)==5:
        return
    multi_result=number1*number2
    result_list3=[int(i) for i in str(multi_result)]
    result_list3.reverse()
    if len(result_list3)==5:
        return
    #print(len(number_list1),len(number_list2),len(result_list1),len(result_list2),len(result_list3))
    col=number_list1[0]+number_list2[0]+result_list1[0]+result_list2[0]+result_list3[0]
    for i in range(1,4):
        new_col=number_list1[i]+number_list2[i]+result_list1[i]+result_list2[i]+result_list3[i]
        if new_col!=col:
            return
    return number1,number2,col

for x in range(100,1000):
    for y in range(10,100):
        result=check(x,y)
        if result:
            _,_,col=result
            print(f'{x} * {y} = {x*y}, all columns adding up to {col}.')

# problems occur in this program:
# 1. the order of reverse the list and append new items to the list--solved
# 2. the use of while and if--solved
# 3. in line 45, the range should be (1,4), so I should pay more attention on the range()
# the last on of the range are excluded