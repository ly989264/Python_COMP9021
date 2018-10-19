class Node:
    def __init__(self,value=None):
        if value is not None:
            self.value=value
        else:
            self.value=None
        self.next_node=None
        return


class Linked_list:
    def __init__(self,list=None):
        if list is not None:
            current_node=None
            for each_index in range(len(list)):
                new_node=Node(list[each_index])
                if each_index==0:
                    self.head=new_node
                    current_node=self.head
                else:
                    current_node.next_node=new_node
                    current_node=current_node.next_node
        else:
            self.head=None

    def display(self):
        if self.head is None:
            return
        current_node=self.head
        while current_node:
            print(current_node.value)
            current_node=current_node.next_node
        return

    def nicely_display(self):
        if self.head is None:
            print()
            return
        current_node=self.head
        while current_node.next_node:
            print(f'{current_node.value} -> ',end='')
            current_node=current_node.next_node
        print(f'{current_node.value}')
        return

    def append_element(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head
        while current_node.next_node:
            current_node=current_node.next_node
        current_node.next_node=new_node
        return

    def prepend_element(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            return
        new_node.next_node=self.head
        self.head=new_node
        return

    def insert_element_at_certain_index(self,value,index):
        if index==0:
            self.prepend_element(value)
            return
        current_index=0
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head
        while current_index<index-1 and current_node.next_node:
            current_node=current_node.next_node
            current_index+=1
        if current_node.next_node is None:
            current_node.next_node=new_node
            return
        temp=current_node.next_node
        current_node.next_node=new_node
        new_node.next_node=temp
        return

    def insert_element_after_certain_value(self,target_value,compare_value):
        if self.head is None:
            return
        new_node=Node(target_value)
        current_node=self.head
        flag=False
        while current_node.next_node:
            if current_node.value == compare_value:
                flag=True
                break
            current_node=current_node.next_node
        if flag:
            if current_node.next_node:
                temp=current_node.next_node
                current_node.next_node=new_node
                new_node.next_node=temp
            else:
                current_node.next_node=new_node
        elif current_node.value == compare_value:
            current_node.next_node=new_node
        else:
            print(f'Cannot insert {target_value} after the value {compare_value} because the value {compare_value}'
                  ' does not exist.')
        return

    def insert_element_before_certain_value(self,target_value,compare_value):
        if self.head is None:
            return
        new_node=Node(target_value)
        current_node=self.head
        flag=False
        if current_node.value == compare_value:
            new_node.next_node=self.head
            self.head=new_node
            return
        while current_node.next_node:
            if current_node.next_node.value == compare_value:
                flag=True
                break
            current_node=current_node.next_node
        if flag:
            new_node.next_node=current_node.next_node
            current_node.next_node=new_node
        else:
            print(f'Cannot insert {target_value} before the value {compare_value} because the value {compare_value}'
                  ' does not exist.')
        return

    def append_list(self,list):
        temp_ll=Linked_list(list)
        if self.head is None:
            self.head=temp_ll.head
            return
        current_node=self.head
        while current_node.next_node:
            current_node=current_node.next_node
        current_node.next_node=temp_ll.head
        return

    def prepend_list(self,list):
        temp_ll=Linked_list(list)
        if self.head is None:
            self.head=temp_ll
            return
        current_node_in_temp=temp_ll.head
        while current_node_in_temp.next_node:
            current_node_in_temp=current_node_in_temp.next_node
        current_node_in_temp.next_node=self.head
        self.head=temp_ll.head
        return

    def insert_list_at_certain_index(self,list,index):
        for each_index in range(len(list)):
            self.insert_element_at_certain_index(list[each_index],index)
            index+=1
        return

    def insert_list_after_certain_value(self,list,compare_value):
        if self.head is None:
            return
        temp_ll=Linked_list(list)
        current_node_on_self=self.head
        current_node_on_temp=temp_ll.head
        while current_node_on_temp.next_node:
            current_node_on_temp=current_node_on_temp.next_node
        flag=False
        while current_node_on_self.next_node:
            if current_node_on_self.value == compare_value:
                flag=True
                break
            current_node_on_self=current_node_on_self.next_node
        if flag:
            current_node_on_temp.next_node=current_node_on_self.next_node
            current_node_on_self.next_node=temp_ll.head
            return
        if current_node_on_self.value==compare_value:
            current_node_on_self.next_node=temp_ll.head
        else:
            print(f'Cannot insert list after the value {compare_value} because the value {compare_value}'
                  ' does not exist.')
        return

    def insert_list_before_certain_value(self,list,compare_value):
        if self.head is None:
            return
        temp_ll=Linked_list(list)
        current_node_on_self=self.head
        current_node_on_temp=temp_ll.head
        while current_node_on_temp.next_node:
            current_node_on_temp=current_node_on_temp.next_node
        if current_node_on_self.value == compare_value:
            current_node_on_temp.next_node=current_node_on_self
            self.head=temp_ll.head
            return
        flag=False
        while current_node_on_self.next_node:
            if current_node_on_self.next_node.value == compare_value:
                flag=True
                break
            current_node_on_self=current_node_on_self.next_node
        if flag:
            current_node_on_temp.next_node=current_node_on_self.next_node
            current_node_on_self.next_node=temp_ll.head
            return
        print(f'Cannot insert the list before the value {compare_value} because the value {compare_value}'
              ' does not exist.')
        return

    def sort_with_key(self,key):
        if self.head is None:
            return
        if self.head.next_node is None:
            return
        temp_list=[]
        current_node=self.head
        while current_node:
            temp_list.append(current_node.value)
            current_node=current_node.next_node
        temp_list.sort(key=key)
        new_ll=Linked_list(temp_list)
        self.head=new_ll.head
        return

    def sort_small_first(self):
        self.sort_with_key(lambda x:x)
        return

    def sort_large_first(self):
        self.sort_with_key(lambda x:-x)
        return

    def duplicate(self):
        if self.head is None:
            return Linked_list()
        current_node=self.head
        temp_list=[]
        while current_node:
            temp_list.append(current_node.value)
            current_node=current_node.next_node
        return Linked_list(temp_list)

    def get_length_of_linked_list(self):
        if self.head is None:
            return 0
        count=0
        current_node=self.head
        while current_node:
            count+=1
            current_node=current_node.next_node
        return count

    def get_value_at_certain_index(self,index):
        if index >= self.get_length_of_linked_list():
            print('Index out of value.')
            return
        if self.head is None:
            return
        count=0
        current_node=self.head
        while current_node:
            if count==index:
                return current_node.value
            current_node=current_node.next_node
            count+=1
        return

    def delete_element_at_certain_index(self,index):
        if index>=self.get_length_of_linked_list():
            print('Index out of value.')
            return
        if self.head is None:
            return
        if index==0:
            temp=self.head.next_node
            self.head=temp
            return
        count=0
        current_node=self.head
        while current_node.next_node:
            if count==index-1:
                temp=current_node.next_node.next_node
                current_node.next_node=temp
                return
            current_node=current_node.next_node
            count+=1
        return

    def check_value_in(self,value):
        if self.head is None:
            return False
        current_node=self.head
        while current_node:
            if current_node.value==value:
                return True
            current_node=current_node.next_node
        return False



# testing
ll=Linked_list([1,3,2])
ll.nicely_display()
print(ll.check_value_in(0))
