# Binary tree
# height size(number of nodes) occurs_in_tree occurs_in_bst is_bst insert_in_bst delete_in_bst
# print_binary_tree pre_order_traversal in_order_traversal post_order_traversal


def go_depth(tree):
    if tree.left.value is None and tree.right.value is None:
        return 0
    value_list=[]
    if tree.left.value is not None:
        value_one=go_depth(tree.left)
        value_list.append(value_one)
    if tree.right.value is not None:
        value_two=go_depth(tree.right)
        value_list.append(value_two)
    value_list.sort(reverse=True)
    return value_list[0]+1

class BinaryTree:
    def __init__(self,value=None):
        self.value=value
        if value is None:
            self.left=None
            self.right=None
        else:
            self.left=BinaryTree()
            self.right=BinaryTree()
        return

    def height_v1(self):
        if self.left is None and self.right is None:
            return go_depth(self)
        else:
            return go_depth(self)

    def sub_height_v2(self):
        if self.value is None:
            return 0
        return max(self.left.sub_height_v2(),self.right.sub_height_v2())+1

    def height_v2(self):
        return max(self.left.sub_height_v2(),self.right.sub_height_v2())

    def size(self):
        if self.value is None:
            return 0
        return self.left.size()+self.right.size()+1

    def occurs_in(self,value):
        if self.value is None:
            return False
        if self.value==value:
            return True
        return self.left.occurs_in(value) or self.right.occurs_in(value)

    def occurs_in_bst(self,value):
        if self.value is None:
            return False
        if self.value == value:
            return True
        if self.value > value:
            return self.left.occurs_in_bst(value)
        else:
            return self.right.occurs_in_bst(value)

    def is_bst(self):
        if self.value is None:
            return True
        if self.left.value is not None:
            current_node=self.left
            while current_node.right.value is not None:
                current_node=current_node.right
            if current_node.value>=self.value:
                return False
        if self.right.value is not None:
            current_node=self.right
            while current_node.left.value is not None:
                current_node=current_node.left
            if current_node.value<=self.value:
                return False
        return self.left.is_bst() and self.right.is_bst()

    def occurs_in_re(self,value):
        if self.value is None:
            return False
        if self.value == value:
            return True
        return self.left.occurs_in_re(value) or self.right.occurs_in_re(value)

    def occurs_in_bst_re(self,value):
        if self.value is None:
            return False
        if self.value == value:
            return True
        if value > self.value:
            return self.right.occurs_in_bst_re(value)
        else:
            return self.left.occurs_in_bst_re(value)

    def is_bst_re(self):
        if self.value is None:
            return True
        if self.left.value is not None:
            current_node=self.left
            while current_node.right.value is not None:
                current_node=current_node.right
            if current_node.value > self.value:
                return False
        if self.right.value is not None:
            current_node=self.right
            while current_node.left.value is not None:
                current_node=current_node.left
            if current_node.value < self.value:
                return False
        return self.left.is_bst_re() and self.right.is_bst_re()

    def insert_in_bst(self,value):
        if self.value is None:
            self.value = value
            self.left = BinaryTree()
            self.right = BinaryTree()
            return True
        if self.occurs_in_bst(value):
            print(f'The value {value} has already occurs in the binary tree.')
            return False
        current_node=self
        # father=self
        while current_node.value is not None:
            if current_node.value > value:
                # father=current_node
                current_node=current_node.left
            elif current_node.value < value:
                # father=current_node
                current_node=current_node.right
        current_node.value=value
        current_node.left=BinaryTree()
        current_node.right=BinaryTree()
        return True

    def mode_analysis_in_bst(self,value):
        '''
        :return: -1: the tree is not a binary tree
                  0: the value does not exist in the binary tree
                  1: the value in the binary tree is a node with both left and right children
                  2: the value in the binary tree is a node with only left child
                  3: the value in the binary tree is a node with only right child
                  4: the value in the binary tree is a leaf, with no children
        '''
        if self.value is None:
            return -1
        if not self.is_bst():
            print('The tree is not a binary tree.')
            return -1
        if not self.occurs_in_bst(value):
            print(f'The value {value} does not exist in the binary tree.')
            return 0
        current_node=self
        while current_node.value is not None:
            if current_node.value > value:
                current_node=current_node.left
            elif current_node.value < value:
                current_node=current_node.right
            else:
                break
        if current_node.left.value is not None and current_node.right.value is not None:
            return 1
        elif current_node.left.value is not None and current_node.right.value is None:
            return 2
        elif current_node.left.value is None and current_node.right.value is not None:
            return 3
        else:
            return 4

    def delete_in_bst(self,value):
        code=self.mode_analysis_in_bst(value)
        if code == -1 or code == 0:
            return False
        if code==4:
            if self.value == value:
                self.left=None
                self.right=None
                self.value=None
                return True
            current_node=self
            father=current_node
            while current_node.value is not None:
                if current_node.value > value:
                    father=current_node
                    current_node=current_node.left
                elif current_node.value < value:
                    father=current_node
                    current_node=current_node.right
                else:
                    break
            if father.value > value:
                father.left=BinaryTree()
            elif father.value < value:
                father.right=BinaryTree()
            return True
        elif code==2:
            current_node=self
            father=current_node
            while current_node.value is not None:
                if current_node.value > value:
                    father=current_node
                    current_node=current_node.left
                elif current_node.value < value:
                    father=current_node
                    current_node=current_node.right
                else:
                    break
            if father.value > value:
                father.left=current_node.left
            else:
                father.right=current_node.left
            return True
        elif code==3:
            current_node = self
            father = current_node
            while current_node.value is not None:
                if current_node.value > value:
                    father = current_node
                    current_node = current_node.left
                elif current_node.value < value:
                    father = current_node
                    current_node = current_node.right
                else:
                    break
            if father.value > value:
                father.left = current_node.right
            else:
                father.right = current_node.right
            return True
        else:
            if self.value == value:
                temp = self.left
                temp_father = None
                while temp.right.value is not None:
                    temp_father = temp
                    temp = temp.right
                if temp_father is None:
                    temp.right=self.right
                    self.value=temp.value
                else:
                    temp.right=self.right
                    temp.left=temp_father
                    temp_father.right=BinaryTree()
                    self.value=temp.value
                return True
            father=self
            current_node=self
            while current_node.value is not None:
                if current_node.value > value:
                    father=current_node
                    current_node=current_node.left
                elif current_node.value < value:
                    father=current_node
                    current_node=current_node.right
                else:
                    break
            temp=current_node.left
            temp_father=None
            while temp.right.value is not None:
                temp_father=temp
                temp=temp.right
            if father.value < current_node.value:
                if temp_father is not None:
                    father.right=temp
                    temp.left=temp_father
                    temp.right=current_node.right
                    temp_father.right=BinaryTree()
                else:
                    father.right=temp
                    temp.right=current_node.right
            else:
                if temp_father is not None:
                    father.left=temp
                    temp.left=temp_father
                    temp.right=current_node.right
                    temp_father.right=BinaryTree()
                else:
                    father.left=temp
                    temp.right=current_node.right
            return True

    def preorder_traversal(self):
        if self.value is None:
            return []
        values=[self.value]
        values.extend(self.left.preorder_traversal())
        values.extend(self.right.preorder_traversal())
        return values

    def inorder_traversal(self):
        if self.value is None:
            return []
        values=[]
        values.extend(self.left.inorder_traversal())
        values.append(self.value)
        values.extend(self.right.inorder_traversal())
        return values

    def postorder_traversal(self):
        if self.value is None:
            return []
        values=[]
        values.extend(self.left.postorder_traversal())
        values.extend(self.right.postorder_traversal())
        values.append(self.value)
        return values


# testing
t=BinaryTree(3)
t_l=BinaryTree(2)
t_ll=BinaryTree(1)
t_r=BinaryTree(5)
t_rl=BinaryTree(4)
t_rlr=BinaryTree(6)
t_rr=BinaryTree(6)
t.left=t_l
t.right=t_r
t.left.left=t_ll
t.right.right=t_rr
t.right.left=t_rl
t.right.left.right=t_rlr
print(t.preorder_traversal())
print(t.inorder_traversal())
print(t.postorder_traversal())
print(t_rlr.postorder_traversal())
et=BinaryTree()
print(et.postorder_traversal())