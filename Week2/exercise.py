'''
this program:
if we have a list called L, and L=[1,2,3]
then we should have the print->[2,1,3]
or if we have L=[1,2,3,4]
then we should have the print->[3,1,4,2]
'''

def test(L):
    '''
    >>> test([])
    []
    >>> test([0])
    [0]
    >>> test([0, 1])
    [1, 0]
    >>> test([0, 1, 2])
    [1, 0, 2]
    >>> test([0, 1, 2, 3])
    [2, 0, 3, 1]
    >>> test([0, 1, 2, 3, 4])
    [2, 0, 4, 1, 3]
    '''
    result_list=[]
    if not len(L):
        result_list=L
        return result_list
    result_list.append(L[len(L)//2])
    for i in range(0,len(L)//2):
        left_index=i
        right_index=len(L)-1-i
        result_list.append(L[left_index])
        if right_index==len(L)//2:
            pass
        else:
            result_list.append(L[right_index])
    return result_list

def test2(L):
    '''
    >>> test2([])
    []
    >>> test2([0])
    [0]
    >>> test2([0, 1])
    [1, 0]
    >>> test2([0, 1, 2])
    [1, 0, 2]
    >>> test2([0, 1, 2, 3])
    [2, 0, 3, 1]
    >>> test2([0, 1, 2, 3, 4])
    [2, 0, 4, 1, 3]
    '''
    if not L:
        return []
    L_copy=L.copy()
    M=[]
    M.append(L_copy.pop(len(L_copy)//2))
    while L_copy:
        M.append(L_copy.pop(0))
        if L_copy:
            M.append(L_copy.pop())
    return M

def test3(L):
    '''
    >>> test3([])
    []
    >>> test3([0])
    [0]
    >>> test3([0, 1])
    [1, 0]
    >>> test3([0, 1, 2])
    [1, 0, 2]
    >>> test3([0, 1, 2, 3])
    [2, 0, 3, 1]
    >>> test3([0, 1, 2, 3, 4])
    [2, 0, 4, 1, 3]
    '''
    if not L:
        return []
    L_copy=L.copy()
    M=[L_copy.pop((len(L_copy)//2))]
    while L_copy:
        try:
            M.append(L_copy.pop(0))
            M.append(L_copy.pop())
        except IndexError:
            pass
    return M

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)