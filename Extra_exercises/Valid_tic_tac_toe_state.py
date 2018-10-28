# A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

def judge_status(chess_list):
    total_number_of_star=0
    total_number_of_circle=0
    for each_string in chess_list:
        temp=[]
        for each_char in each_string:
            if each_char=='O':
                total_number_of_circle+=1
            elif each_char=='X':
                total_number_of_star+=1
    if total_number_of_circle>total_number_of_star:
        return False
    if total_number_of_star-total_number_of_circle not in [0,1]:
        return False
    x_win_number=0
    y_win_number=0
    temp=[[] for _ in range(3)]
    for each_string in chess_list:
        if each_string=='XXX':
            x_win_number+=1
        elif each_string=='OOO':
            y_win_number+=1
        for each_index in range(3):
            temp[each_index].append(each_string[each_index])
    for each in temp:
        if each=='XXX':
            x_win_number+=1
        elif each=='OOO':
            y_win_number+=1
    t1=chess_list[0][0]+chess_list[1][1]+chess_list[2][2]
    t2=chess_list[0][2]+chess_list[1][1]+chess_list[2][0]
    if t1=='XXX':
        x_win_number+=1
    if t1=='OOO':
        y_win_number+=1
    if t2=='XXX':
        x_win_number+=1
    if t2=='OOO':
        y_win_number+=1
    if x_win_number*y_win_number!=0:
        return False
    return True

print(judge_status(["XOX", "O O", "XOX"]))