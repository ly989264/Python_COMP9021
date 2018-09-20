from extended_linked_list import *
from random import seed,randrange

def collect_nodes(L, length):
    node = L.head
    nodes = {}
    for _ in range(length):
        nodes[id(node)] = node.value
        node = node.next_node
    return nodes

with open('quiz_8_result.txt','w') as f:
    for each_seed in range(1,11):
        for each_length in [11,13,17,19]:
            for each_step in [2,3,4,5,6,7,8,9,10]:
                print(f'------{each_seed}-{each_length}-{each_step}------',file=f)
                seed(each_seed)
                L = [randrange(100) for _ in range(each_length)]
                LL = ExtendedLinkedList(L)
                LL.print(f)
                nodes = collect_nodes(LL, each_length)
                LL.rearrange(each_step)
                if collect_nodes(LL, each_length) != nodes:
                    print('You cheated!',file=f)
                else:
                    LL.print(f)
                print('$$$$$$$$$$$$',file=f)