# Decodes all multiplications of the form
#
#                        2  1  0    number_list1
#                   x       1  0    number_list2
#                     ----------
#                     3  2  1  0    result_list
#                     6  5  4
#                     ----------
#                     a  9  8  7
#
# such that the sum of all digits in all 4 columns is constant.


# Insert your code here.
# Method 1
def check(number1,number2):# number1: XXX number2: XX
    number_list1=[i for i in str(number1)]
    number_list2=[i for i in str(number2)]
    number_list1.reverse()
    number_list2.reverse()
    result_list=[]
    temp=0
    count_list=[]
    for each in number_list2:
        count=0
        for i in number_list1:
            wenter,remainer=multi(int(each),int(i))
            result_list.append(remainer+temp)
            temp=wenter
            count+=1
            if temp and count==3:
                count+=1
                result_list.append(temp)
        count_list.append(count)
        temp=0
    if count_list[0]==3:
        new_result_list=result_list[0:3]
        new_result_list.append(0)
        new_result_list+=result_list[3:]
        del result_list
        result_list=new_result_list
        del new_result_list
    if count_list[1]==4:
        return None
        #result_list.pop()
    temp=0
    result_list.append(result_list[0])
    wenter,remainer=add(result_list[1],result_list[4])
    result_list.append(remainer+temp)
    temp=wenter
    wenter, remainer = add(result_list[2], result_list[5])
    result_list.append(remainer + temp)
    temp = wenter
    wenter, remainer = add(result_list[3], result_list[6])
    result_list.append(remainer + temp)
    col1=int(number_list1[0])+int(number_list2[0])+result_list[0]+result_list[7]
    col2=int(number_list1[1])+int(number_list2[1])+result_list[1]+result_list[4]+result_list[8]
    col3=int(number_list1[2])+result_list[2]+result_list[5]+result_list[9]
    col4=result_list[3]+result_list[6]+result_list[10]
    if col1==col2 and col1==col3 and col1==col4:
        return number1,number2,col1
    else:
        return None

def multi(number1,number2):# take two numbers as arguments and return the tuple of the result of multiple
    result=number1*number2
    return divmod(result,10)

def add(number1,number2):
    return divmod((number1+number2),10)

for x in range(100,1000):
    for y in range(10,100):
        result=check(x,y)
        if result:
            _,_,col=result
            print(f'{x} * {y} = {x*y}, all columns adding up to {col}.')
