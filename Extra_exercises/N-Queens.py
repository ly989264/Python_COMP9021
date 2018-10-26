from copy import deepcopy

def generate_grid(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def self_abs(n):
    if n<0:
        return -1*n
    return n

def fill_certain_queen(first_coordinate,second_coordinate,grid,n):
    for i in range(n):
        if grid[first_coordinate][i]==1 and i!=second_coordinate:
            print('a')
            return False
        elif grid[first_coordinate][i]==0:
            grid[first_coordinate][i]=2
        if grid[i][second_coordinate]==1 and i!=first_coordinate:
            print('b')
            return False
        elif grid[i][second_coordinate]==0:
            grid[i][second_coordinate]=2
    for i in range(n):
        for j in range(n):
            if self_abs(i-first_coordinate)==self_abs(j-second_coordinate):
                if grid[i][j]==1 and i!=first_coordinate and j!=second_coordinate:
                    print('c')
                    return False
                elif grid[i][j]==0:
                    grid[i][j]=2
    return True

def operate(grid,level,n):
    # print(level)
    global final_list
    if level>=n:
        final_list.append(grid)
        return
    for i in range(n):
        if grid[level][i]==0:
            new_grid=deepcopy(grid)
            new_grid[level][i]=1
            if not fill_certain_queen(level,i,new_grid,n):
                continue
            operate(new_grid,level+1,n)
    return


grid=generate_grid(8)
final_list=[]
operate(grid,0,8)
print(len(final_list))