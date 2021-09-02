# Priority queue using heap
# Author: Y.

class PriorityQueue(object):

    # Create an empty queue (heap)
    def __init__(self, arr=[]):
        self._queue = arr
        self._size = 0

    # Heapify the tree
    def max_heapify(self, arr, length, ind):
        largest = ind
        l = ind * 2 + 1
        r = ind * 2 + 2

        # Find the largest among root, left child and right child
        if l < length and arr[l] > arr[largest]:
            largest = l
        if r < length and arr[r] > arr[largest]:
            largest = r
        
        # Swap and continue heapifying if root is not largest
        if largest != ind:
            arr[largest], arr[ind] = arr[ind], arr[largest]
            self.max_heapify(arr, length, largest)

    # Insert data into tree
    def add(self, item):
        if self._size == 0:
            self._queue.append(item)
            self._size += 1
        else:
            self._queue.append(item)
            self._size += 1
            for i in (self._size//2-1, -1, -1):
                self.max_heapify(self._queue, self._size, i)
        
    # Delete data from the tree
    def remove(self, item):
        if self._size == 0:
            print("The queue is empty\n")
            return
        
        # Find out the index of item
        i = 0
        for i in range(0, self._size):
            if self._queue[i] == item:
                break
        
        # Swap and remove the item
        self._queue[i], self._queue[self._size-1] = self._queue[self._size-1], self._queue[i]
        self._queue.pop()
        self._size -= 1

        # heapify again
        for i in range(self._size//2-1, -1, -1):
            self.max_heapify(self._queue, self._size, i)


if __name__=="__main__":

    obj = PriorityQueue()

    obj.add(3)
    obj.add(4)
    obj.add(9)
    obj.add(5)
    obj.add(2)
    print(obj._queue)

    obj.remove(4)
    print(obj._queue)

    obj.remove(5)
    print(obj._queue)