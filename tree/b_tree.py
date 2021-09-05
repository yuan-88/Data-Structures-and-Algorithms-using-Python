# B Tree including functions of Insert, Search, Delete, Print
# Author: Y.

# Create Node class for B Tree
class BTreeNode(object):
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []
        self.child = []

# Create B Tree class
class BTree(object):
    def __init__(self, t):
        # For root: 1 <= # keys <= 2t-1,   2 <= # child <= 2t
        # For non-root: t-1 <= # keys <= 2t-1,  t <= # child <= 2t
        self._root = BTreeNode(is_leaf=True)
        self._t = t
    
# =============== INSERT PROCESS =============== #
    # Split root if root is full, otherwise, search from root
    def insert_key(self, key):
        # If root is full, then split root
        if len(self._root.keys) == (2*self._t - 1):
            # Create a new node and set it as root
            z = BTreeNode(is_leaf=False)
            temp = self._root
            self._root = z
            # Insert the previous root into z.child
            z.child.insert(0, temp)
            # Split z.child[0], i.e. previous root
            self.split(z, 0)
            # Insert key into the tree
            self.insert_non_full(z, key)
        # If root is not full, then insert key into the tree
        else:
            self.insert_non_full(self._root, key)

    # Insert key into the corresponding position
    def insert_non_full(self, x, key):
        i = len(x.keys) - 1
        # If x is leaf, insert new key into the correct position
        if x.is_leaf:
            # If new key is less than current key, then move current key to the right side
            x.keys.append(None)
            while i >= 0 and key < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            # Insert new key into the correct position
            x.keys[i+1] = key
        # If x is not a leaf, then find out corresponding child
        # until find out corresponding position in the leaf layer
        else:
            while i >= 0 and key < x.keys[i]:
                i -= 1
            i += 1
            # If the founded child is full, then split the child
            if len(x.child[i].keys) == (2*self._t - 1):
                self.split(x, i)
                # The middle key from the child will be added to the front of ith key,
                # Thus, need to compare new key to the added middle key of child.
                # If new key is greater than the added key, then move index to right.
                if key > x.keys[i]:
                    i += 1
            # Continue to search corresponding position on child layer
            self.insert_non_full(x.child[i], key)

    # Split layer
    def split(self, x, i):
        t = self._t
        # Get ith child of x
        y = x.child[i]
        # Create new node 'z'
        z = BTreeNode(is_leaf=y.is_leaf)
        # Insert new node 'z' into x (i+1)th child position
        x.child.insert(i+1, z)
        # Insert the middle key from child y into x ith key position
        x.keys.insert(i, y.keys[t-1])
        # Add right half of y's keys (y.keys[t:2t-1]) to z
        z.keys = y.keys[t:2*t-1]
        # Add left half of y's keys (y.keys[0:t-1]) to y
        y.keys = y.keys[0:t-1]
        # If y is leaf, split y's child into y and z
        if not y.is_leaf:
            # Add right half of y's child (y.child[t:2t]) to z
            z.child = y.child[t:2*t]
            # Add left half of y's child (y.child[0:t]) to y
            y.child = y.child[0:t]

# =============== SEARCH PROCESS =============== #
    # Search key
    def search_key(self, x, key):
        if x is not None:
            i = 0
            while i < len(x.keys) and key > x.keys[i]:
                i += 1

            if i < len(x.keys) and key == x.keys[i]:
                print(f'Found key!  keys:{x.keys}, index:{i}')
                return (x.keys, i)
            elif x.is_leaf:
                return None
            else:
                return self.search_key(x.child[i], key)
        else:
            self.search_key(self._root, key)

# =============== PRINT PROCESS =============== #
    # Print out tree
    def print_tree(self, x, level=0):
        print(f'level: {level}, # keys: {len(x.keys)}, keys:', end=' ')
        for key in x.keys:
            print(key, end=' ')
        print()
        level += 1
        if len(x.child) > 0:
            for child in x.child:
                self.print_tree(child, level)

# =============== DELETE PROCESS =============== #
    # Delete a key
    def delete_key(self, x, key):
        t = self._t
        i = 0
        while i < len(x.keys) and key > x.keys[i]:
            i += 1
        
        # Case1: If the key is founded in the leaf layer, just delete it
        if x.is_leaf:
            if i < len(x.keys) and key == x.keys[i]:
                x.keys.pop(i)
                return True
            return False
        # Case2: If the key is founded in the internal layer, do internal deletion process
        if i < len(x.keys) and key == x.keys[i]:
            return self.delete_internal_key(x, key, i)
        # Case3: If the key not found in the current layer, but need to search one child,
        #        and the child's keys are enough (more than t), then continue to check the child
        elif len(x.child[i].keys) >= t:
            return self.delete_key(x.child[i], key)
        # Case4: If the key is not found in the current layer, but need to search one child,
        #        and the child layer's keys are not enough, then borrow key or do merge firstly, and continue to check the child.
        else: 
            # If it is a internal child of the curren layer
            if i != 0 and i + 2 < len(x.child):
                # Check if we can borrow a key from left neighbor subtree
                if len(x.child[i-1].keys) >= t:
                    self.delete_sibling(x, i, i-1)
                # Check if we can borrow a key from right neighbor subtree
                elif len(x.child[i+1].keys) >= t:
                    self.delete_sibling(x, i , i+1)
                # Merge current subtree and right neighbor subtree
                else:
                    self.delete_merge(x, i, i+1)
            # If it is a left-end child of the current layer
            elif i == 0:
                # Check if we can borrow a key from right neighbor subtree
                if len(x.child[i+1].keys) >= t:
                    self.delete_sibling(x, i, i+1)
                # Merge current subtree and rigth neighbor subtree
                else:
                    self.delete_merge(x, i, i+1)
            # If it is a right-end child of the current layer
            elif i + 1 == len(x.child):
                print(x.keys, i)
                # Check if we can borrow a key from left neighbor subtree
                if len(x.child[i-1].keys) >= t:
                    self.delete_sibling(x, i, i-1)
                # Merge current subtree and left neighbor subtree
                else:
                    self.delete_merge(x, i, i-1)
                    i -= 1
            # Continue to check the corresponding child
            return self.delete_key(x.child[i], key)

    # The key is founded in the internal layer, and delete it
    def delete_internal_key(self, x, key, i):
        t = self._t
        if x.is_leaf:
            if key == x.keys[i]:
                x.keys.pop(i)
                return
            return
        
        # Since if we delete a key in the internal layer, it will affect the child pointers, 
        # need to deal with this issue. and there are mainly 3 options.

        # Case2-1: the key is replaced by an inorder predecessor,
        # if the left child has more than the minimum number of keys. 
        if len(x.child[i].keys) >= t:
            x.keys[i] = self.delete_predecessor(x.child[i])
            return
        # Case2-2: the key is replaced by an inorder successor,
        # if the right child has more than the minimum number of keys.
        elif len(x.child[i+1].keys) >= t:
            x.keys[i] = self.delete_successor(x.child[i+1]) 
            return
        # Case2-3: If either child has exactly a minimum number of keys,
        # merge the left and the right children firstly, and repeat internal deletion process for the child layer. 
        else:
            self.delete_merge(x, i, i+1)
            self.delete_internal_key(x.child[i], key, self._t-1)

    # For Case2-1 of internal deletion process. Replace target key by inorder predecessor
    def delete_predecessor(self, x):
        # If x is leaf, return the last key of x to replace the target key to be deleted.
        if x.is_leaf:
            return x.keys.pop()
        
        # If x is not leaf, continue to search the inorder predecessor in leaf layer
        n = len(x.keys) - 1
        if len(x.child[n].keys) >= self._t:
            self.delete_sibling(x, n+1, n)
        else:
            self.delete_merge(x, n, n+1)
        return self.delete_predecessor(x.child[n+1])

    # For Case2-2 of internal deletion process. Replace target key by inorder successor
    def delete_successor(self, x):
        # If x is leaf, return the last key of x to replace the target key to be deleted.
        if x.is_leaf:
            return x.keys.pop(0)

        # If x is not leaf, continue to search the inorder successor in leaf layer
        if len(x.child[1].keys) >= self._t:
            self.delete_sibling(x, 0, 1)
        else:
            self.delete_merge(x, 0, 1)
        return self.delete_successor(x.child[0])

    # Delete the sibling process
    def delete_sibling(self, x, i, j):
        """
        - x.child[i] will be deleted
        - x.keys[i] will replace x.child[i]
        - x.child[j] will replace x.keys[i]
        """
        # The target key will be deleted
        cnode = x.child[i]
        # If borrow key from right side
        if i < j:
            rsnode = x.child[j]
            # Use parent key x.keys[i] to replace target key x.child[i]
            cnode.keys.append(x.keys[i])
            # Use the first key of right side child x.child[j][0] to replace parent key x.keys[i]
            x.keys[i] = rsnode.keys[0]
            # If there is a child in the first key of right side child x.child[j][0],
            # add the child to right side of target key, since the right side child key has been removed.
            if len(rsnode.child) > 0:
                cnode.child.append(rsnode.child[0])
                rsnode.child.pop(0)
            rsnode.keys.pop(0)
        # The same process for the case of left side
        else:
            lsnode = x.child[j]
            cnode.keys.insert(0, x.keys[i-1])
            x.keys[i-1] = lsnode.keys.pop()
            if len(lsnode.child) > 0:
                cnode.child.insert(0, lsnode.child.pop())

    # Merge left child(x.child[i]), parent key(x.keys[i]), right child(x.child[i+1])
    def delete_merge(self, x, i, j):
        cnode = x.child[i]
        if j > i:
            rsnode = x.child[j]
            cnode.keys.append(x.keys[i])
            for k in range(len(rsnode.keys)):
                cnode.keys.append(rsnode.keys[k])
                if len(rsnode.child) > 0:
                    cnode.child.append(rsnode.child[k])
            if len(rsnode.child) > 0:
                cnode.child.append(rsnode.child.pop())
            new = cnode
            x.keys.pop(i)
            x.child.pop(j)
        else:
            lsnode = x.child[j]
            lsnode.keys.append(x.keys[j])
            for k in range(len(cnode.keys)):
                lsnode.keys.append(cnode.keys[k])
                if len(cnode.child) > 0:
                    lsnode.child.append(cnode.child[k])
            if len(cnode.child) > 0:
                lsnode.child.append(cnode.child.pop())
            new = lsnode
            x.keys.pop(j)
            x.child.pop(i)
        
        if x == self._root and len(x.keys) == 0:
            self._root = new


if __name__=="__main__":

    b = BTree(3)

    print("\n===== Insert test =====")
    for i in range(20):
        b.insert_key(i)
    b.print_tree(b._root)

    print("\n===== Search test =====")
    print(b.search_key(x=b._root, key=8))

    print("\n===== Delete test =====") 
    print(b.delete_key(b._root, 79))
    b.print_tree(b._root)
    print()
    print(b.delete_key(b._root, 8))
    b.print_tree(b._root)
