# implement linked list by myself
import sys

class New_Node:
    def __init__(self,value):
        self.value=value
        self.next_node=None
    def __str__(self):
        return f'Node type, value: {self.value}, next node: {id(next_node)}'
    def __repr__(self):
        return f'Node type, id: {id(self)}'

class New_LinkedList:
    def __init__(self, l = None, key = lambda x:x):
        self.key=key
        if not l:# which means that list is None
            self.head=None
        else:
            if len(l)==1:
                self.head=New_Node(l[0])
                self.head.next_node=None
            else:
                self.head=New_Node(l[0])
                self.head.next_node=None
                current_node_in_linked_list=self.head
                for each_index in range(1,len(l)):
                    current_node_in_linked_list.next_node=New_Node(l[each_index])
                    current_node_in_linked_list=current_node_in_linked_list.next_node
    def print(self,file=sys.stdout,separator=','):
        temp_list=[]
        current_node=self.head
        while current_node:
            temp_list.append(current_node.value)
            current_node = current_node.next_node
        print(separator.join(str(i) for i in temp_list),file=file)
    def duplicate(self):
        if not self.head:
        duplicate_linked_list=New_LinkedList()


# testing
LL=New_LinkedList([1,2,3,4,5,6])
LL.print(separator='---')