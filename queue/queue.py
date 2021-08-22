# Queue implementation using Array
# Author: Yuan

# Create a queue class
class Queue(object):
    
    # Create an empty Queue
    def __init__(self):
        self.queue = []

    # Size of Queue
    def size(self):
        return len(self.queue)

    # Check if Queue is empty
    def is_empty(self):
        return self.size() == 0

    # Push data to Queue
    def enqueue(self, item):
        self.queue.append(item)

    # Pop data from Queue
    def dequeue(self):
        return self.queue.pop(0)

    # Print the whole queue
    def get(self):
        return list(reversed(self.queue[:]))

    
if __name__=="__main__":
    q = Queue()
    arr = [1,3,4,2,5]

    print(q.is_empty())

    for i in arr:
        q.enqueue(int(i))
        
    print("queue: ", q.get())
    print("1st deq: ", q.dequeue())
    print("queue: ", q.get()) 
    print("2nd deq: ", q.dequeue())
    
    q.enqueue(4)
    print("queue: ", q.get())
    print("3rd get: ", q.dequeue())
    print("queue: ", q.get())
    