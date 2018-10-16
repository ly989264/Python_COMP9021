
'''
Implements a function that takes as input an iterable L of nonnegative integers and an integer N,
and displays all ways of inserting negations and parentheses in L, resulting in an expression
that evaluates to N.
'''


def subtractions(L, N):
    pass
    # replace pass above with your code
    for expression in possible_subtractions(L):
        if eval(expression) == N:
            print(expression[1: -1])

# Possibly define other functions