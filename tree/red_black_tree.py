# Red-Black Tree
# Author: Y.

import sys

# Create node class
class Node(object):
    def __init__(self, key=None, color='red', parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left, self.right = left, right
        self.color = color   # red or black

class RedBlackTree(object):

    def __init__(self):
        self.NIL = Node(key=None, color='black')
        self._root = self.NIL

# ======== INSERT PROCESS ======== #
    def left_rotation(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self._root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        x.parent = y
        y.left = x

    def right_rotation(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self._root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        x.parent = y
        y.right = x
    
    # Insert a new key to tree
    def insert(self, key):
        # Assign NIL to the left and right child of new Node
        new_node = Node(key=key, left=self.NIL, right=self.NIL, color='red')

        # Let x be the root, Let y be the leaf(NIL)
        x = self._root
        y = None

        # Check if the tree is empty, if yes, insert new Node as a root
        # Else, repeat following steps until leaf (NIL) is reached
        #   - Comapre new key with root key
        #   - go right subtree if key > root key, otherwise, go left
        while x != self.NIL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        # Assign the parent of the leaf as a parent of new Node
        new_node.parent = y
        # If leaf key is greater than new key, make new Node as right child
        # otherwise, make new Node as left child
        if y == None:
            self._root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node
        
        if new_node.parent is None:
            new_node.color = 'black'
            return
        if new_node.parent.parent is None:
            return
        self.insert_fixup(new_node)
    
    # Fix up Red-Black tree after insertion
    def insert_fixup(self, new_node):
        curr_node = new_node
        while curr_node.parent.color == 'red':
            # If parent of curr node is the left child of grand parent of curr node
            if curr_node.parent == curr_node.parent.parent.left:
                # If the color of parent's sibling is 'red',
                # set both parent and parent's sibling color as 'black'
                # set grand parent color as 'red' 
                if curr_node.parent.parent.right.color == 'red':
                    curr_node.parent.parent.left.color = 'black'
                    curr_node.parent.parent.right.color = 'black'
                    curr_node.parent.parent.color = 'red'
                    # Assign grand parent to curr node
                    curr_node = curr_node.parent.parent
                # If parent's sibling is not exist or the color is 'black', do following.
                else:
                    # If curr node is the right child of parent,
                    # exchange curr node and parent, and do left rotation.
                    # Then the parent will become the left child of the curr node
                    if curr_node == curr_node.parent.right:
                        curr_node = curr_node.parent
                        self.left_rotation(curr_node)
                    # Do right rotation and set two new child (parent and grand parent) color as 'red',
                    # set new parent (new node) color as 'black'
                    curr_node.parent.color = 'black'
                    curr_node.parent.parent.color = 'red'
                    self.right_rotation(curr_node.parent.parent)
            # If parent of curr node is the right child of grand parent of curr node
            else:
                if curr_node.parent.parent.left.color == 'red':
                    curr_node.parent.parent.left.color = 'black'
                    curr_node.parent.parent.right.color = 'black'
                    curr_node.parent.parent.color = 'red'
                    curr_node = curr_node.parent.parent
                else:
                    if curr_node == curr_node.parent.left:
                        curr_node = curr_node.parent
                        self.right_rotation(curr_node)
                    curr_node.parent.color = 'black'
                    curr_node.parent.parent.color = 'red'
                    self.left_rotation(curr_node.parent.parent)
            if curr_node == self._root:
                break
        self._root.color = 'black'

# ======= PRINT PROCESS ======= #
    def print_tree(self, node=None, indent='', last=True):
        if node is None:
            node = self._root

        if node != self.NIL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(str(node.key) + "(" + node.color + ")")
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

# ======= SEARCH PROCESS ====== #
    def search_key(self, node=None, key=None):
        node = self._root if node==None else node

        if node == self.NIL or node.key == key:
            return node
        
        if key > node.key:
            return self.search_key(node.right, key)
        return self.search_key(node.left, key)
    
# ======= DELETE PROCESS ====== #
    def delete_key(self, node=None, key=None):
        if node == None:
            node = self._root

        # Find target node
        target = self.search_key(node=node, key=key)
        if target == self.NIL:
            print("Cannot find key")
            return
        
        # If there is only left child for target,
        # Use right child to replace target
        if target.left == self.NIL:
            x = target.right
            self.transplant(target, target.right)
        # If there is only right child of target,
        # Use left child to replace target
        elif target.right == self.NIL:
            x = target.left
            self.transplant(target, target.left)
        else:
            # Assign minimum of right subtree of target into y
            successor = self.get_successor(target.right)
            print(f'successor: {successor.key}')
            # Save successor color
            successor_color = successor.color
            print(f'successor color: {successor.color}')
            # Assign right child of y into x
            x = successor.right
            if successor.parent == target:
                x.parent = successor
            # if successor is not a child of target
            else:
                self.transplant(successor, successor.right)
                successor.right = target.right
                successor.right.parent = successor
            
            self.transplant(target, successor)
            successor.left = target.left
            successor.left.parent = successor
            successor.color = target.color
        if successor_color == 'black':
            self.print_tree()
            print(x.key)
            self.delete_fixup(x)
    
    def delete_fixup(self, node):
        while node != self._root and node.color == 'black':
            # Case1: If node is the left child of parent, and color is black
            if node == node.parent.left:
                sibling = node.parent.right
                # Case1-1: If color of sibling is red.
                #   Step1: Set parent color as red, sibling color as black
                #   Step2: Do left rotation for parent, so that node will be new parent.
                #   Step3: Find new sibling for node
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.left_rotation(node.parent)
                    sibling = node.parent.right

                # Case1-2: If color of both two child of sibling is black.
                #   Step1: Set sibling color as red
                #   Step2: Set parent as new node, and continue the process
                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    # Case1-3: If right child of sibling is black, left child of sibling is red
                    #   Step1: Exchange colors between left child and sibling, and do right-rotation
                    if sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.right_rotation(sibling)
                        sibling = sibling.parent
                    # Case1-4: If right child of sibling is red, left child of sibling is black
                    #   Step1: Exchange colors between left child and sibling, and do right-rotation
                    sibling.color = sibling.parent.color
                    sibling.right.color = 'black'
                    node.parent.color = 'black'
                    self.left_rotation(node.parent)
                    node = self._root
            else:
                sibling = node.parent.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.right_rotation(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == 'black' and sibling.left.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.left_rotation(sibling)
                        sibling = sibling.parent
                    sibling.color = node.parent.color
                    sibling.left.color = 'black'
                    node.parent.color = 'black'
                    self.right_rotation(node.parent)
                    node = self._root
        node.color = 'black'

    def transplant(self, x, y):
        if x.parent == None:
            self._root = x
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.parent = x.parent
            
    def get_successor(self, x=None):
        if self._root == self.NIL:
            return None
        if x == None:
            x = self._root
        while x.left != self.NIL:
            x = x.left
        return x
        
    def get_predecessor(self, x=None):
        if self._root == self.NIL:
            return None
        if x == None:
            x = self._root
        while x.right != self.NIL:
            x = x.right
        return x.key

if __name__=='__main__':
    
    bst = RedBlackTree()

    bst.insert(55)
    bst.insert(40)
    bst.insert(65)
    bst.insert(60)
    bst.insert(75)
    bst.insert(57)
    bst.insert(30)

    bst.print_tree()

    res_node = bst.search_key(key=60)
    print(res_node.key, res_node.color)

    bst.delete_key(key=65)

    bst.print_tree()