# Tree implementation
# Author: Y.

# Define a tree node class
class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree(object):

    # Create a empty binary tree
    def __init__(self, root = None):
        super(BinaryTree, self).__init__()
        self._root = root

    # Add data to binary tree
    def add(self, item):
        node = Node(item)
        if self._root == None:
            self._root = node
        else:
            queue = []
            queue.append(self._root)
            while True:
                curr = queue.pop(0)
                if curr.left == None:
                    curr.left = node
                    return
                elif curr.right == None:
                    curr.right = node
                    return
                else:
                    queue.append(curr.left)
                    queue.append(curr.right)
    
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
    tree = BinaryTree()

    for i in range(10):
        tree.add(i)
    
    print("\n[preorder]")
    print(tree.preorder())
    print(tree.preorder(tree._root.left))

    print("\n[inorder]")
    print(tree.inorder())
    print(tree.inorder(tree._root.left))

    print("\n[postorder]")
    print(tree.postorder())
    print(tree.postorder(tree._root.left))

    print("\n[Breadth First Search]")
    print(tree.bfs())
    print(tree.bfs(tree._root.left))
