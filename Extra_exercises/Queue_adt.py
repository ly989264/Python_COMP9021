# Queue

class Queue:
    def __init__(self):
        self._list=[]

    def push_into_queue(self,value):
        self._list.append(value)
        return True

    def read_value(self):
        if not self._list:
            return None
        return self._list[0]

    def pull_out_queue(self):
        if not self._list:
            return False
        self._list.pop(0)
        return True

# testing
if __name__=='__main__':
    q=Queue()
    print(q.read_value())
    q.push_into_queue(1)
    q.push_into_queue(2)
    q.push_into_queue(5)
    print(q.read_value())
    q.pull_out_queue()
    print(q.read_value())