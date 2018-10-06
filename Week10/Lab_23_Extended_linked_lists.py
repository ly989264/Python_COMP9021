# Extend the module linked_list_adt.py which is part of the material of the 8th lecture into a
# module extended_linked_list_adt.py to implement the extra method remove_duplicates(),
# that keeps only the first occurrence of any value. As for the 8th quiz, this should be done without
# creating new nodes and without using Python lists.

# Written by z5190675

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicates(self):
        node=self.head
        if not node:
            return
        if not node.next_node:# the linked list is empty
            return
        # if not node.next_node.next_node:# the linked list has only one element
        #     return
        already_list=[node.value]
        while node.next_node.next_node:
            if node.next_node.value not in already_list:
                already_list.append(node.next_node.value)
                node = node.next_node
            else:
                temp=node.next_node.next_node
                node.next_node=temp
                # do not use node=node.next_node here!
        if node.next_node.value in already_list:
            node.next_node=None
        return

# # testing
# LL=ExtendedLinkedList([1,2,3])
# LL.remove_duplicates()
# LL.print()
# LL=ExtendedLinkedList([1,1,1,2,1,2,1,2,3,3,2,1])
# LL.remove_duplicates()
# LL.print()
# LL=ExtendedLinkedList()
# LL.remove_duplicates()
# LL.print()
# LL=ExtendedLinkedList([1,1])
# LL.remove_duplicates()
# LL.print()