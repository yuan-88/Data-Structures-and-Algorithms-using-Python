# Linked list: Single Linked List, Double Linked List, Circular Linked List
# Author: Y.

# Define a linked list node class
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

# Create a Single Linked List class
class SingleLinkedList(object):

    # Create a empty linked list
    def __init__(self):
        super(SingleLinkedList, self).__init__()
        self._head = None
        self._size = 0
    
    # Check if linked list is empty
    def is_empty(self):
        return self._head == None
    
    # Length of linked list by traversing through linked list
    # O(n) time complexity
    def length(self):
        cnt = 0
        curr = self._head
        while curr != None:
            cnt += 1
            curr = curr.next
        return cnt
    
    # Length of linked list by traversing through linked list
    # O(1) time complexity
    def size(self):
        return self._size

    # Traverse the whole linked list
    def travel(self):
        curr = self._head
        while curr != None:
            print(curr.item, end=" ")
            curr = curr.next
        print('\n')

    # Add data to the head of linked list
    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node
        self._size += 1
    
    # Add data to the end of linked list
    def append(self, item):
        node = Node(item)
        curr = self._head
        while curr.next != None:
            curr = curr.next
        curr.next = node
        self._size += 1

    # Insert data to linked list
    def insert(self, pos, item):
        node = Node(item)
        cnt = 0
        curr = self._head
        while pos != (cnt + 1):
            curr = curr.next
            cnt += 1
        node.next = curr.next
        curr.next = node
        self._size += 1

    # Search data from linked list
    def search(self, item):
        cnt = 0
        curr = self._head
        while curr.item != item and curr.next != None:
            curr = curr.next
            cnt += 1
        if curr.item == None:
            return False
        else:
            return cnt

    # Delete data from linked list
    def remove(self, item):
        curr = self._head
        while curr.next.item != item and curr.next != None:
            curr = curr.next
        if curr.next == None:
            return False
        else:
            temp = curr.next
            curr.next = temp.next
            self._size -= 1
    
    # Reverse linked list
    def reverse(self):
        prev = None
        curr = self._head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self._head = prev


# Create a Double Linked List class
class DoubleLinkedList(object):

    # Create a empty linked list
    def __init__(self):
        super(DoubleLinkedList, self).__init__()
        self._head = None
        self._size = 0

    # Check if linked list is empty
    def is_empty(self):
        return self._head == None

    # Length of linked list by traversing through linked list
    # O(n) time complexity
    def length(self):
        cnt = 0
        curr = self._head
        while curr != None:
            cnt += 1
            curr = curr.next
        return cnt
    
    # Length of linked list by traversing through linked list
    # O(1) time complexity
    def size(self):
        return self._size

    # Traverse the whole linked list
    def travel(self):
        curr = self._head
        while curr != None:
            print(curr.item, end=" ")
            curr = curr.next
        print("\n")

    # Add data to the head of linked list
    def add(self, item):
        node = Node(item)
        node.next = self._head
        # different from single ll, need to add node to current _head.prev
        if not self.is_empty():
            self._head.prev = node
        self._head = node
        self._size += 1
    
    # Add data to the end of linked list
    def append(self, item):
        node = Node(item)
        curr = self._head
        while curr.next != None:
            curr = curr.next
        curr.next = node
        node.prev = curr
        self._size += 1

    # Insert data to linked list
    def insert(self, pos, item):
        if pos < 0:
            print("invalid position.")
            return -1
        elif pos == 0:
            self.add(item)
        elif pos == self.length():
            self.append(item)
        else:
            node = Node(item)
            cnt = 0
            curr = self._head
            while pos != (cnt + 1):
                curr = curr.next
                cnt += 1
            node.next = curr.next
            if curr.next != None:
                curr.next.prev = node
            curr.next = node
            node.prev = curr
            self._size += 1

    # Search data from linked list    
    def search(self, item):
        cnt = 0
        curr = self._head
        while curr.item != item and curr.next != None:
            curr = curr.next
            cnt += 1
        if curr.item == None:
            return False
        else:
            return cnt

    # Delete data from linked list
    def remove(self, item):
        curr = self._head
        while curr.next.item != item and curr.next != None:
            curr = curr.next
        if curr.next == None:
            return False
        else:
            temp = curr.next
            curr.next = temp.next
            temp.next.prev = curr
            self._size -= 1
    
    # Reverse linked list
    def reverse(self):
        prev = None
        curr = self._head
        while curr:
            next_node = curr.next
            curr.next = prev
            curr.prev = next_node
            prev = curr
            curr = next_node
        self._head = prev


# Create a Cercular Linked List class
class CercularLinkedList(object):

    # Create a empty linked list
    def __init__(self):
        super(CercularLinkedList, self).__init__()
        self._head = None
        self._tail = None
        self._size = 0
    
    # Check if linked list is empty
    def is_empty(self):
        return self._head == None

    # Length of linked list by traversing through linked list
    # O(n) time complexity
    def length(self):
        cnt = 0
        curr = self._head
        while curr != self._tail:
            cnt += 1
            curr = curr.next
        return cnt+1
    
    # Length of linked list by traversing through linked list
    # O(1) time complexity
    def size(self):
        return self._size

    # Traverse the whole linked list
    def travel(self):
        curr = self._head
        while curr != self._tail:
            print(curr.item, end=" ")
            curr = curr.next
        print(curr.item, end="\n")

    # Add data to the head of linked list
    def add(self, item):
        node = Node(item)
        if self._head is None:
            self._head = node
            self._tail = node
            self._head.next = self._tail
            self._tail.next = self._head
        else:
            # current tail will point to new node
            self._tail.next = node
            # new node will point to head
            node.next = self._head
            # new node will become new head
            self._head = node
        self._size += 1

    # Add data to the end of linked list
    def append(self, item):
        node = Node(item)
        if self._head is None:
            self._head = node
            self._tail = node
            self._head.next = self._tail
            self._tail.next = self._head
        else:
            # current tail will point to new node
            self._tail.next = node
            # new node will become new tail
            self._tail = node
            # new tail(new node) will point to head
            self._tail.next = self._head
        self._size += 1

    # Insert data to linked list
    def insert(self, pos, item):
        node = Node(item)
        cnt = 0
        curr = self._head
        while pos != (cnt + 1):
            curr = curr.next
            cnt += 1
        node.next = curr.next
        curr.next = node
        self._size += 1

    # Search data from linked list    
    def search(self, item):
        cnt = 0
        curr = self._head
        while curr.item != item and curr != self._tail:
            curr = curr.next
            cnt += 1
        if curr.item != item:
            return False
        else:
            return cnt

    # Delete data from linked list
    def remove(self, item):
        if self._head.item == item:
            self._head = self._head.next
            self._tail.next = self._head
        else:
            curr = self._head
            while curr.next.item != item and curr != self._tail:
                curr = curr.next
            if curr.next.item != item:
                return False
            else:
                temp = curr.next
                curr.next = temp.next
                self._size -= 1
    
    # Reverse linked list
    def reverse(self):
        prev = self._tail
        curr = self._head
        while curr != self._tail:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self._tail = curr.next
        curr.next = prev
        self._head = curr


if __name__ == "__main__":

    # Test for Single Linked List
    print("====== Test for Single Linked List ======")

    ll = SingleLinkedList()
    print(ll.is_empty())

    ll.add(1); ll.travel()
    ll.add(2); ll.travel()
    ll.append(3); ll.travel()
    ll.insert(2, 4); ll.travel()
    ll.insert(4, 5); ll.travel()

    print(ll.is_empty())
    print("length:", ll.length())

    print(ll.search(3))
    print(ll.search(5))
    
    ll.remove(1)
    print("length:", ll.length())
    print("size:", ll.size())
    ll.travel()

    ll.reverse()
    print("length:", ll.length())
    print("size:", ll.size())
    ll.travel()


    # Test for Double Linked List
    print("\n====== Test for Double Linked List ======")
    
    dll = DoubleLinkedList()
    print("size:", dll.size())
    print(dll.is_empty())

    dll.add(1); dll.travel()
    dll.add(2); dll.travel()
    dll.append(3); dll.travel()
    dll.insert(2, 4); dll.travel()
    dll.insert(4, 5); dll.travel()

    print(dll.is_empty())
    print("length:", dll.length())
    print("size:", dll.size())

    print(dll.search(3))
    print(dll.search(5))
    
    dll.remove(1)
    print("length:", dll.length())
    print("size:", dll.size())
    dll.travel()

    dll.reverse()
    print("length:", dll.length())
    print("size:", dll.size())
    dll.travel()


    # Test for Cercular Linked List
    print("\n====== Test for Cercular Linked List ======")
    
    cll = CercularLinkedList()
    print("size:", cll.size())
    print(cll.is_empty())

    cll.add(1); cll.travel()
    cll.add(2); cll.travel()
    cll.add(7); cll.travel()
    cll.append(3); cll.travel()
    cll.append(6); cll.travel()
    cll.insert(2, 4); cll.travel()
    cll.insert(4, 5); cll.travel()

    print(cll.is_empty())
    print("length:", cll.length())
    print("size:", cll.size())

    print(cll.search(3))
    print(cll.search(5))
    
    cll.remove(1)
    print("length:", cll.length())
    print("size:", cll.size())
    cll.travel()

    cll.reverse()
    print("size:", cll.size())
    cll.travel()
    print("length:", cll.length())
    