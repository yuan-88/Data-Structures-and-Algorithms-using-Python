# Binary Search Tree including functions of DFS, BFS
# Author: Y.

# Define node class for binary search tree
class Node(object):    
    def __init__(self, item=None):
        self.item = item
        self.left = None
        self.right = None


# Create binary search tree
class BinarySearchTree(object):

    # Create an empty binary search tree
    def __init__(self, root=None):
        super(BinarySearchTree, self).__init__()
        if root is None:
            self._root = root
        else:
            self._root = Node(root)

    # Add data to tree
    def add(self, item):
        if self._root is None:
            self._root = Node(item)
        else:
            self._add(item, self._root)
    
    def _add(self, item, root):
        # If new item is less than root
        if item < root.item:
            if root.left is None:
                root.left = Node(item)
            else:
                self._add(item, root.left)

        # If new item is greater than root
        elif item > root.item:
            if root.right is None:
                root.right = Node(item)
            else:
                self._add(item, root.right)
        else:
            print("Value already in tree")
    
    # Depth First Search(DFS)   
    # DFS: Preorder (Root -> Left -> Right)
    def preorder(self, root='root'):
        if root == 'root':
            root = self._root
        if root == None:
            return
        print(root.item, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    # DFS: Inorder (Left -> Root -> Right)
    def inorder(self, root='root'):
        if root == 'root':
            root = self._root
        if root == None:
            return
        self.inorder(root.left)
        print(root.item, end=' ')        
        self.inorder(root.right)
    
    # DFS: Postorder (Left -> Right -> Root)
    def postorder(self, root='root'):
        if root == 'root':
            root = self._root
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right) 
        print(root.item, end=' ')

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
    
    bst = BinarySearchTree()

    from random import randint
    for _ in range(10):
        i = randint(0, 100)
        bst.add(i)
    
    print("\n[preorder]")
    print(bst.preorder())
    print(bst.preorder(bst._root.left))

    print("\n[inorder]")
    print(bst.inorder())
    print(bst.inorder(bst._root.left))

    print("\n[postorder]")
    print(bst.postorder())
    print(bst.postorder(bst._root.left))

    print("\n[Breadth First Search]")
    print(bst.bfs())
    print(bst.bfs(bst._root.left))