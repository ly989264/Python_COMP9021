# A Doubly Linked List abstract data type
#
# Written by Eric Martin for COMP9021


from copy import deepcopy


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    # Creates a linked list possibly from a list of values.
    def __init__(self, L=None, key=lambda x: x):
        self.key = key
        if L is None:
            self.head = None
            return
        # If L is not subscriptable, then will generate an exception that reads:
        # TypeError: 'type_of_L' object is not subscriptable
        if not len(L[: 1]):
            self.head = None
            return
        node = Node(L[0])
        self.head = node
        for e in L[1:]:
            node.next_node = Node(e)
            node.next_node.previous_node = node
            node = node.next_node

    def print(self, separator=', '):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.print(separator = ' : ')
        2 : 0 : 1 : 3 : 7
        '''
        if not self.head:# which means that the linked list is empty
            print()
            return
        node=self.head
        current_list=[]
        while node.next_node:
            current_list.append(node.value)
            node=node.next_node
        current_list.append(node.value)
        # print(current_list)
        print(separator.join(str(i) for i in current_list))
        return

    def duplicate(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL_copy = LL.duplicate()
        >>> LL_copy.print()
        2, 0, 1, 3, 7
        '''
        if not self.head:# means that the linked list is empty
            return
        new_l=DoublyLinkedList(key=self.key)
        current_node=self.head
        node_copy=Node(deepcopy(current_node.value))
        new_l.head=node_copy
        last_node=None
        while current_node.next_node:
            current_node=current_node.next_node
            node_copy.next_node=Node(deepcopy(current_node.value))
            node_copy.previous_node=last_node
            last_node=node_copy
            node_copy=node_copy.next_node
        return new_l

    def length(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> print(LL.length())
        5
        '''
        if not self.head:# means that the linked list is empty
            return 0
        node = self.head
        current_length=1
        while node.next_node:
            node=node.next_node
            current_length+=1
        return current_length

    def apply_function(self, function):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.apply_function(lambda x: 2 * x)
        >>> LL.print()
        4, 0, 2, 6, 14
        '''
        if not self.head:# means that the linked list is empty
            return
        node=self.head
        node.value=function(node.value)
        while node.next_node:
            node=node.next_node
            node.value=function(node.value)
        return

    def is_sorted(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> print(LL.is_sorted())
        False
        '''
        if not self.head:# means that the linked list is empty
            return True
        flag=True
        direction=None
        node=self.head
        last_one=node.value
        while node.next_node:
            node=node.next_node
            if not direction:
                if node.value>last_one:
                    direction='r'
                elif node.value<last_one:
                    direction='l'
                else:
                    pass
            else:
                if direction=='r' and node.value<last_one:
                    flag=False
                    break
                elif direction=='l' and node.value>last_one:
                    flag=False
                    break
            last_one=node.value
        self.direction=direction
        return flag


    def extend(self, LL):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.extend(LL.duplicate())
        >>> LL.print()
        2, 0, 1, 3, 7, 2, 0, 1, 3, 7
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.extend(DoublyLinkedList([]))
        >>> LL.print()
        2, 0, 1, 3, 7
        '''
        if not LL.head:# means that LL is empty
            return
        if not self.head:# means that the linked list is empty
            return
        node=self.head
        while node.next_node:
            node=node.next_node
        # now the node is the last one of the original linked list
        LL.head.previous_node=node
        node.next_node=LL.head
        return


    def reverse(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7, 2, 0, 1, 3, 7])
        >>> LL.reverse()
        >>> LL.print()
        7, 3, 1, 0, 2, 7, 3, 1, 0, 2
        '''
        if not self.head:# means that the linked list is empty
            return
        node=self.head
        while node.next_node:
            node=node.next_node
        # now node is the last node of the linked list
        reverse_list=[]
        reverse_list.append(node.value)
        while node.previous_node:
            node=node.previous_node
            reverse_list.append(node.value)
        temp=DoublyLinkedList(reverse_list)
        self.head=temp.head
        return

    def index_of_value(self, value):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> print(LL.index_of_value(2))
        4
        >>> print(LL.index_of_value(5))
        -1
        '''
        if not self.head:# means that the linked list is empty
            return -1
        node=self.head
        current_index=0
        if node.value==value:
            return current_index
        while node.next_node:
            node=node.next_node
            current_index+=1
            if node.value==value:
                return current_index
        return -1

    def value_at(self, index):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> print(LL.value_at(4))
        2
        >>> print(LL.value_at(10))
        None
        '''
        if not self.head:# means that the linked list is empty
            return None
        node=self.head
        current_index=0
        if current_index==index:
            return node.value
        while node.next_node:
            node=node.next_node
            current_index+=1
            if current_index==index:
                return node.value
        return None

    def prepend(self, LL):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> LL.prepend(DoublyLinkedList([20, 21, 22]))
        >>> LL.print()
        20, 21, 22, 7, 3, 1, 0, 2, 7, 3, 1, 0, 2
        '''
        if not self.head:# means that the linked list is empty
            return
        if not LL.head:# means that LL is empty
            return
        original_head=self.head
        self.head=LL.head
        node=self.head
        while node.next_node:
            node=node.next_node
        # now node is the last node of LL
        node.next_node=original_head
        original_head.previous_node=node
        return

    def append(self, value):
        '''
        >>> LL = DoublyLinkedList()
        >>> LL.append(10)
        >>> LL.print()
        10
        >>> LL.append(15)
        >>> LL.print()
        10, 15
        '''
        if not self.head:# means that the linked list is empty
            self.head=Node(value)
            return
        new_node=Node(value)
        node=self.head
        while node.next_node:
            node=node.next_node
        # now node is the last node of the linked list
        node.next_node=new_node
        new_node.previous_node=node
        return

    def insert_value_at(self, value, index):
        '''
        >>> LL = DoublyLinkedList([10, 15])
        >>> LL.insert_value_at(5, 0)
        >>> LL.insert_value_at(25, 3)
        >>> LL.insert_value_at(20, 3)
        >>> LL.print()
        5, 10, 15, 20, 25
        '''
        if not self.head:# means that the linked list is empty
            if index==0:
                self.head=Node(value)
            return
        if index==0:
            new_node=Node(value)
            original_head=self.head
            self.head=new_node
            self.head.next_node=original_head
            original_head.previous_node=self.head
            return
        node=self.head
        current_index=0
        new_node=Node(value)
        if current_index==index-1:
            new_node.next_node=node.next_node
            if node.next_node:
                node.next_node.previous_node=new_node
            node.next_node=new_node
            new_node.previous_node=node
            return
        while node.next_node:
            # print(current_index)
            node=node.next_node
            current_index+=1
            if current_index==index-1:
                new_node.next_node=node.next_node
                if node.next_node:
                    node.next_node.previous_node=new_node
                node.next_node=new_node
                new_node.previous_node=node
                return
        return

    def insert_value_before(self, value_1, value_2):
        '''
        >>> LL = DoublyLinkedList([5, 10, 15, 20, 25])
        >>> LL.insert_value_before(0, 5)
        True
        >>> LL.insert_value_before(30, 35)
        False
        >>> LL.insert_value_before(22, 25)
        True
        >>> LL.insert_value_before(7, 10)
        True
        >>> LL.print()
        0, 5, 7, 10, 15, 20, 22, 25
        '''
        if not self.head:# means that the linked list is empty
            return False
        node=self.head
        new_node=Node(value_1)
        if node.value==value_2:
            original_head=self.head
            self.head=new_node
            new_node.next_node=original_head
            original_head.previous_node=self.head
            return True
        if node.next_node.value==value_2:
            new_node.next_node=node.next_node
            if node.next_node:
                node.next_node.previous_node=new_node
            node.next_node=new_node
            new_node.previous_node=node
            return True
        while node.next_node.next_node:
            node=node.next_node
            if node.next_node.value == value_2:
                new_node.next_node = node.next_node
                if node.next_node:
                    node.next_node.previous_node = new_node
                node.next_node = new_node
                new_node.previous_node = node
                return True
        return False

    def insert_value_after(self, value_1, value_2):
        '''
        >>> LL = DoublyLinkedList([0, 5, 7, 10, 15, 20, 22, 25])
        >>> LL.insert_value_after(3, 1)
        False
        >>> LL.insert_value_after(2, 0)
        True
        >>> LL.insert_value_after(12, 10)
        True
        >>> LL.insert_value_after(27, 25)
        True
        >>> LL.print()
        0, 2, 5, 7, 10, 12, 15, 20, 22, 25, 27

        '''
        if not self.head:# means that the linked list is empty
            return False
        node=self.head
        new_node=Node(value_1)
        if node.value==value_2:
            new_node.next_node=node.next_node
            if node.next_node:
                node.next_node.previous_node=new_node
            node.next_node=new_node
            new_node.previous_node=node
            return True
        while node.next_node:
            node=node.next_node
            if node.value==value_2:
                new_node.next_node = node.next_node
                if node.next_node:
                    node.next_node.previous_node = new_node
                node.next_node = new_node
                new_node.previous_node = node
                return True
        return False

    def insert_sorted_value(self, value):
        '''
        >>> LL = DoublyLinkedList([0, 2, 5, 7, 10, 12, 15, 20, 22, 25, 27])
        >>> LL.insert_sorted_value(-5)
        >>> LL.insert_sorted_value(17)
        >>> LL.insert_sorted_value(30)
        >>> LL.print()
        -5, 0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30

        '''
        if not self.head:# means that the linked list is empty
            return
        node=self.head
        new_node=Node(value)
        if self.is_sorted():
            direction=self.direction
            if direction=='r':
                if not node.next_node:
                    if node.value>value:
                        node.next_node=new_node
                        new_node.previous_node=node
                        return
                    else:
                        new_node.next_node=self.head
                        self.head.previous_node=new_node
                        self.head=new_node
                        return
                else:
                    while node.next_node:
                        if node.value>value:
                            new_node.next_node = self.head
                            self.head.previous_node = new_node
                            self.head = new_node
                            return
                        if node.value<value and node.next_node.value>value:
                            self.insert_value_after(value,node.value)
                            return
                        node=node.next_node
                    node.next_node=new_node
                    new_node.previous_node=node
            elif direction=='l':
                if not node.next_node:
                    if node.value<value:
                        node.next_node=new_node
                        new_node.previous_node=node
                        return
                    else:
                        new_node.next_node=self.head
                        self.head.previous_node=new_node
                        self.head=new_node
                        return
                else:
                    while node.next_node:
                        if node.value<value:
                            new_node.next_node = self.head
                            self.head.previous_node = new_node
                            self.head = new_node
                            return
                        if node.value>value and node.next_node.value<value:
                            self.insert_value_after(value,node.value)
                            return
                        node=node.next_node
                    node.next_node=new_node
                    new_node.previous_node=node
            else:
                new_node.next_node = self.head
                self.head.previous_node = new_node
                self.head = new_node
                return

    def delete_value(self, value):
        '''
        >>> LL = DoublyLinkedList([-5, 0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30])
        >>> LL.delete_value(-5)
        True
        >>> LL.delete_value(30)
        True
        >>> LL.delete_value(15)
        True
        >>> LL.print()
        0, 2, 5, 7, 10, 12, 17, 20, 22, 25, 27

        '''
        if not self.head:# means that the linked list is empty
            return False
        node=self.head
        if node.value==value and node.next_node==None:# means that the linked list only has one node
            node.value=None
            return True
        if node.value==value:# the first node is the target node
            self.head=node.next_node
            self.head.previous_node=None
            return True
        while node.next_node.next_node:
            if node.next_node.value==value:
                node.next_node=node.next_node.next_node
                node.next_node.previous_node=node
                return True
            node=node.next_node
        if node.next_node.value==value:
            node.next_node=None
            return True
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
