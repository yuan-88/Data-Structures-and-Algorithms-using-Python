# Circular queue using Array
# Author: Y.

# Create a circular queue class
class CircularQueue(object):

    # Create an empty queue
    def __init__(self, size):
        self._size = size
        self._queue = [None] * self._size
        self._head = self._tail = -1

    # Insert data into the queue
    def enqueue(self, item):
        # if size = 5, tail = 4, head = 0
        if ((self._tail + 1) % self._size == self._head):
            print("The circular queue is full\n")
        elif self._head == -1:
            self._head = 0
            self._tail = 0
            self._queue[self._tail] = item
        else:
            self._tail = (self._tail + 1) % self._size
            self._queue[self._tail] = item
    
    # Delete data from the queue
    def dequeue(self):
        if self._head ==  -1:
            print("The circular queue is emtpy\n")
        elif self._tail == self._head:
            tmp = self._queue[self._head]
            self._tail, self._head = -1, -1
            return tmp
        else:
            tmp = self._queue[self._head]
            self._head = (self._head + 1) % self._size
            return tmp

    # Print queue
    def print_queue(self):
        if self._head == -1:
            print("The circular queue is emtpy\n")
        elif self._tail >= self._head:
            for i in range(self._head, self._tail+1):
                print(self._queue[i], end=' ')
            print()
        else:
            for i in range(self._head, self._size):
                print(self._queue[i], end=' ')
            for i in range(0, self._tail+1):
                print(self._queue[i], end=' ')
            print()
        

if __name__=="__main__":

    # Test queue
    obj = CircularQueue(5)
    obj.print_queue()
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)
    obj.enqueue(5)
    
    print("Initial queue")
    obj.print_queue()

    obj.dequeue()
    print("After removing an element from the queue")
    obj.print_queue()
