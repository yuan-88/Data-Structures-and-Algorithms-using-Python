# AVL Tree 
# Author: Y.

# Create node class for AVL Tree
class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.left = None
        self.right = None
        self.height = 1

# Create AVL Tree class
class AVLTree(object):

    # Create an empty tree
    def __init__(self, root=None):
        self._root = root

    # Add data to tree
    def add(self, root='root', item=None):
        # If the head is empty, add data to head
        if self._root is None:
            self._root = Node(item)
            return

        # Set head as root
        if root == 'root':
            root = self._root
        
        # Insert the node into the correct location
        if root is None:
            return Node(item)
        elif item < root.item:
            root.left = self.add(root.left, item)
        else:
            root.right = self.add(root.right, item)
        
        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor
        balance_factor = self.get_balance(root)

        # Right rotation if new node is added to left side
        # and left depth is larger than right depth
        if balance_factor > 1:
            if item < root.left.item:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        
        # Left rotation if new node is added to right side
        # and right depth is larger than left depth
        if balance_factor < -1:
            if item > root.right.item:
                return self.left_rotate(root)
            else:
                root.right =  self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    # Get height of node
    def get_height(self, root):
        if root is None:
            return 0
        return root.height
    
    # Get balance factor of node
    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    # Exchange parent node and right child node
    def left_rotate(self, node):
        """
        Args
            node: current parent node
        
        Return
            new parent node
        """
        # Get right child of parent node
        r_node = node.right
        # Get left child of above right child
        tmp = r_node.left
        # change parent node and left child 
        r_node.left = node
        node.right = tmp
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        r_node.height = 1 + max(self.get_height(r_node.left), self.get_height(r_node.right))

        return r_node
    
    # Exchange parent node and left child 
    def right_rotate(self, node):
        """
        Args
            node: current parent node
        
        Return
            new parent node
        """
        # Get left child of parent node
        l_node = node.left
        # Get right child of above left child
        tmp = l_node.right
        # Change parent node and left child
        l_node.right = node
        node.left = tmp

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        l_node.height = 1 + max(self.get_height(l_node.left), self.get_height(l_node.right))

        return l_node

    # Breadth First Search(BFS)
    def bfs(self, root='root'):
        if root == 'root':
            root = self._root
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.item, end=' ')
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


if __name__=="__main__":

    tree = AVLTree()
    root = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11, 10, 15]
    for num in nums:
        root = tree.add(item=num)
        print(tree.bfs())
    
    print(root.item, root.left.item, root.right.item)
    print(root.left.left.item, root.left.right.item)
    print(root.left.left.left.item, root.left.left.right.item)
    print(root.right.right.item)