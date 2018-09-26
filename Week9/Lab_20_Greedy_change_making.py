# Prompts the user for an amount, and outputs the minimal number of banknotes
# needed to match that amount, as well as the detail of how many banknotes
# of each type value are used.
# The available banknotes have a face value which is one of
# $1, $2, $5, $10, $20, $50, and $100.


# Insert your code here

desired_amount=int(input('Input the desired amount: '))
print()
face_value_list=[100,50,20,10,5,2,1]
face_nb_list=[]
current_index=0
while desired_amount:
    face_nb_list.append(desired_amount//face_value_list[current_index])
    desired_amount=desired_amount%face_value_list[current_index]
    current_index+=1
total=0
for each_element in face_nb_list:
    total+=each_element
if total==1:
    print('1 banknote is needed.')
else:
    print(f'{total} banknotes are needed.')
print('The detail is:')
for each_index in range(len(face_nb_list)):
    if face_nb_list[each_index]!=0:
        if len(str(face_value_list[each_index]))==3:
            print(f'${face_value_list[each_index]}: {face_nb_list[each_index]}')
        elif len(str(face_value_list[each_index]))==2:
            print(f' ${face_value_list[each_index]}: {face_nb_list[each_index]}')
        else:
            print(f'  ${face_value_list[each_index]}: {face_nb_list[each_index]}')