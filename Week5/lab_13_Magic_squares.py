# Given a positive integer n, a magic square of order n is a matrix of size n x n
# that stores all numbers from 1 up to n^2 and such that the sum of the n rows,
# the sum of the n columns, and the sum of the two diagonals is constant,
# hence equal to n(n^2+1)/2.


def is_magic_square(square):
    '''
    check whether the square is a magic square
    :param square: a list with the format [[i,i,i],[i,i,i],[i,i,i]]
    :return:True or False
    '''
    n=len(square)
    expect_value=n*(n*n+1)/2
    for each in range(0,n):
        sum=0
        for eachin in square[each]:
            sum+=eachin
        if sum!=expect_value:
            return False
        sum=0
        for eachver in range(0,n):
            sum+=square[eachver][each]
        if sum!=expect_value:
            return False
    sum=0
    for i in range(0,n):
        sum+=square[i][i]
    if sum!=expect_value:
        return False
    total=n-1
    sum=0
    for i in range(0,n):
        second_index=total-i
        sum+=square[i][second_index]
    if sum!=expect_value:
        return False
    return True

def print_square(square):
    '''
    print square
    :param square: a list with the format [[i,i,i],[i,i,i],[i,i,i]]
    :return:None
    '''
    if len(square)==1:
        print(square[0][0])
    else:
        for eachline in range(0,len(square)):
            for eachbeforeindex in range(0,len(square)-1):
                print(f'{square[eachline][eachbeforeindex]} ',end='')
            print(f'{square[eachline][-1]}')
    return
