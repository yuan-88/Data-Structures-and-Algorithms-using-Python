# Deque using Array
# Author: Y.

# Create Double Ended Queue
class Deque(object):

    # Create an empty queue
    def __init__(self):
        self._queue = []

    # Add data to front
    def add_front(self, item):
        self._queue.insert(0, item)
    
    # Add data to Rear
    def add_rear(self, item):
        self._queue.append(item)
    
    # Remove data form front
    def remove_front(self):
        return self._queue.pop(0)
    
    # Remove data from Rear
    def remove_rear(self):
        return self._queue.pop()

    # Return queue size
    def size(self):
        return len(self._queue)


if __name__=="__main__":

    d = Deque()
    print(d.size())
    d.add_rear(8)
    d.add_rear(5)
    d.add_front(7)
    d.add_front(10)
    d.add_rear(11)
    print(d.size())
    print(d._queue)
    print(d.remove_rear())
    print(d.remove_front())
    print(d._queue)
    d.add_front(55)
    d.add_rear(45)
    print(d._queue)