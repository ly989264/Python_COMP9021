# Stack

class Stack:
    def __init__(self):
        self._list=[]

    def push_in_stack(self,value):
        self._list.append(value)
        return True

    def pull_out_stack(self):
        return self._list.pop(-1)

    def read_last_element(self):
        if not self._list:
            return None
        else:
            return self._list[-1]

# testing
if __name__=='__main__':
    stack=Stack()
    stack.push_in_stack(1)
    stack.push_in_stack(2)
    stack.push_in_stack(5)
    print(stack.pull_out_stack())
    print(stack.pull_out_stack())