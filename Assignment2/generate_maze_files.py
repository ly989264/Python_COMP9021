# THIS PROGRAM IS USED TO GENERATE DIFFERENT MAZE FILES TO TEST THE MAZE PROGRAM
# THIS FILE IS USED FOR TESTING THE PROGRAM

import os
from random import seed,randrange

os.chdir('maze_test_file')

# CREATE VALID MAZE FILE OF X FROM 2 TO 31, Y FROM 2 TO 41
count=0
for seed in range(1,6):
    seed(seed)# PAY ATTENTION, THE FILES GENERATED BEFORE DID NOT HAVE THIS
    for x in range(2,32):
        for y in range(2,42):
            filename=f'maze_{count}.txt'
            with open(filename,'w') as f:
                for each_row in range(0,x-1):
                    temp_list=[randrange(0,4) for _ in range(0,y-1)]
                    temp_list.append(randrange(0,3,2))
                    nb_of_spaces=randrange(0,3)
                    space_string=' '*nb_of_spaces
                    print(space_string.join(str(i) for i in temp_list),file=f)
                # last row
                temp_list=[randrange(0,2) for _ in range(0,y-1)]
                temp_list.append(0)
                nb_of_spaces = randrange(0, 3)
                space_string = ' ' * nb_of_spaces
                print(space_string.join(str(i) for i in temp_list), file=f)
            count+=1
