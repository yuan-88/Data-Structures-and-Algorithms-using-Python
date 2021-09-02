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
        if x.parent == self.NIL:
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

    # Print
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
