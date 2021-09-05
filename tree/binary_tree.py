# Binary Tree including funcitons of  DFS, BFS, Check Full, Complete, Perfect, Balanced
# Author: Y.

# Create Node class for binary tree
class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.left = None
        self.right = None

# Create Binary tree class
class BinaryTree(object):

    # Create an empty binary tree
    def __init__(self, root=None):
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

    # Check if the tree is full
    # Every internal node has either two or no children
    def is_full_tree(self, root='root'):
        if root == 'root':
            root = self._root

        if root is None:
            return True
        
        # Check if the parent node has no children
        if root.left is None and root.right is None:
            return True
        
        # Check if the parent node has either two children
        if root.left is not None and root.right is not None:
            return self.is_full_tree(root.left) and self.is_full_tree(root.right)
        
        return False
    
    # Check if a tree is complete using number of nodes and index
    # All the levels are completely filled except possibly the lowest one, which is filled from the left
    # Get numbers of nodes
    def count_nodes(self, root='root'):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    # Check if it is a complete tree
    def is_complete_tree(self, root='root', index=0, num_nodes=0):
        if root == 'root':
            root = self._root
            num_nodes = self.count_nodes(root)
        
        if root is None:
            return True
        
        if index >= num_nodes:
            return False
        
        return self.is_complete_tree(root.left, 2 * index + 1, num_nodes) \
            and self.is_complete_tree(root.right, 2 * index + 2, num_nodes)
    

    # Check if a tree is perfect using depth of tree and level
    # Every internal node has exactly two child nodes and all the leaf nodes are at the same level
    # Get depth of a tree
    def depth(self, root):
        d = 0
        while root is not None:
            d += 1
            root = root.left
        return d

    # Check if it is a perfect tree
    def is_perfect_tree(self, root='root', d=0, level=0):
        if root == 'root':
            root = self._root
            d = self.depth(root)

        if root is None:
            return True
        
        # Check the level, if the parent node has no children, 
        if root.left is None and root.right is None:
            return level+1 == d
        
        # Check the sub tree if the parent node has two children
        if root.left is not None and root.right is not None:
            return self.is_perfect_tree(root.left, d, level+1) and self.is_perfect_tree(root.right, d, level+1)
        
        return False

    # Check if the tree is balanced using height
    # The height of the left and right subtree of any node differ by not more than 1
    def get_height(self, root='root'):
        if root is None:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def is_balanced_tree(self, root='root', height=0):
        if root == 'root':
            root = self._root
            height = 0
        
        if root is None:
            return True
        
        return abs(self.get_height(root.left)-self.get_height(root.right)) < 2 \
            and self.is_balanced_tree(root.left) \
            and self.is_balanced_tree(root.right)

            
            
if __name__=="__main__":
    tree = BinaryTree()

    for i in range(15):
        tree.add(i)
    
    print('\n====== Check DFS ======')
    print("\n[preorder]")
    print(tree.preorder())
    print(tree.preorder(tree._root.left))

    print("\n[inorder]")
    print(tree.inorder())
    print(tree.inorder(tree._root.left))

    print("\n[postorder]")
    print(tree.postorder())
    print(tree.postorder(tree._root.left))

    print('\n====== Check BFS ======')
    print("\n[Breadth First Search]")
    print(tree.bfs())
    print(tree.bfs(tree._root.left))

    print('\n====== Check binary tree types ======')
    print(f'Full tree: {tree.is_full_tree()}')
    print(f'Perfect tree: {tree.is_perfect_tree()}')
    print(f'Complete tree: {tree.is_complete_tree()}')
    print(f'Balanced: {tree.is_balanced_tree()}')