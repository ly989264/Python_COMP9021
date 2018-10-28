# Stack
class Stack:
    def __init__(self):
        self.slist=[]

    def __len__(self):
        return len(self.slist)

    def is_empty(self):
        if not self.slist:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.slist[-1]

    def push(self,value):
        self.slist.append(value)
        return True

    def pop(self):
        if self.is_empty():
            return False
        else:
            return self.slist.pop()

# testing
if __name__=='__main__':
    stack=Stack()
    print(stack.is_empty())
    print(stack.push(2))
    print(stack.is_empty())
    print(stack.peek())
    print(stack.push(3))
    print(stack.push(1))
    print(stack.is_empty())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())