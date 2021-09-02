# Stack using Array
# Author: Y.

# Create a stack class
class Stack(object):

    # Create an empty Stack
    def __init__(self):
        self.stack = []

    # Size of Stack
    def size(self):
        return len(self.stack)
    
    # Check if Stack is empty
    def is_empty(self):
        return self.size() == 0
    
    # Push data to Stack
    def push(self, item):
        self.stack.append(item)

    # Pop data from Stack
    def pop(self):
        return self.stack.pop()

    # Travel Stack
    def travel(self):
        return self.stack[:]
    
    # Check the value at the peek
    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    # Clear Stack
    def clear(self):
        del self.stack[:]


if __name__=="__main__":
    s = Stack()

    arr = [1,3,4,2,5]
    
    print(s.is_empty())

    for i in arr:
        s.push(i)
    
    print("stack: ", s.travel())
    print(s.peek())
    
    print("1st pop: ", s.pop())
    print("stack: ", s.travel()) 
    
    print("2nd pop: ", s.pop())
    print("stack: ", s.travel())
    
    s.push(4)
    print("stack: ", s.travel())

    print("3rd pop: ", s.pop())
    print("stack: ", s.travel())

    s.clear()
    print("stack: ", s.travel())
