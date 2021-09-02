# Heap implementation
# Author: Y.

from typing import List

class Heap(object):
    """Pure implementation of the heap sort algorithm in python

    Args:
        arr(list): some mutable ordered list with comparable items inside
    
    Returns:
        the same list ordered by ascending

    Examples:
    >>> heap = Heap()
    >>> arr = [3, 2, 1, 4]
    >>> heap.heap_sort(arr)
    >>> print(arr)
    [1, 2, 3, 4]

    >>> arr = [2]
    >>> heap.heap_sort(arr)
    >>> print(arr)
    [2]

    >>> arr = [-2, -5, -45]
    >>> heap.heap_sort(arr)
    >>> print(arr)
    [-45, -5, -2]
    """

    def __init__(self):
        super(Heap, self).__init__()

    # Sort list by heap sort
    def heap_sort(self, arr, type='max-heap'):
        if len(arr) < 2:
            return
        else:
            n = len(arr)

            if type == 'max-heap':
                # Build a max heap
                for i in range(n//2-1, -1, -1):
                    self._max_heapify(arr, n, i)
                # Extract elements one by one
                for i in range(n-1, 0, -1): 
                    arr[i], arr[0] = arr[0], arr[i]
                    self._max_heapify(arr, i, 0)

            elif type == 'min-heap':
                # Build a min heap
                for i in range(n//2-1, -1, -1):
                    self._min_heapify(arr, n, i)
                # Extract elements one by one
                for i in range(n-1, 0, -1): 
                    arr[i], arr[0] = arr[0], arr[i]
                    self._min_heapify(arr, i, 0)
            else:
                print('Invalid type')
                return

    # Create a max heap
    def _max_heapify(self, arr: List[int], length: int, index: int) -> List[int]:
        l = index * 2 + 1
        r = index * 2 + 2
        largest = index

        # Compare current node to left child,
        # If the left child is greater than the current node,
        # Set left child as the current node
        if l < length and arr[l] > arr[largest]:
            largest = l

        # Compare current node to right child,
        # If the right child is greater than the current node,
        # Set right child as the current node
        if r < length and arr[r] > arr[largest]:
            largest = r

        # If parent value less than child value,
        # Exchange parent and child
        if largest != index:
            arr[largest], arr[index] = arr[index], arr[largest]
            self._max_heapify(arr, length, largest)

    # Create a min heap
    def _min_heapify(self, arr: List[int], length: int, index: int) -> List[int]:
        l = index * 2 + 1
        r = index * 2 + 2
        least = index

        # Compare current node to left child,
        # If the left child is greater than the current node,
        # Set left child as the current node
        if l < length and arr[l] < arr[least]:
            least = l

        # Compare current node to right child,
        # If the right child is greater than the current node,
        # Set right child as the current node
        if r < length and arr[r] < arr[least]:
            least = r

        # If parent value less than child value,
        # Exchange parent and child
        if least != index:
            arr[least], arr[index] = arr[index], arr[least]
            self._min_heapify(arr, length, least)


if __name__=="__main__":

    heap = Heap()

    # Test max heap
    import numpy as np
    arr = np.random.randint(0, 100, 7)
    print(arr)
    heap.heap_sort(arr, type='max-heap')
    print(arr)

    arr = [2]
    heap.heap_sort(arr, type='max-heap')
    print(arr)


    # Test min heap
    arr = np.random.randint(0, 100, 7)
    print(arr)
    heap.heap_sort(arr, type='min-heap')
    print(arr)

    arr = [2]
    heap.heap_sort(arr, type='min-heap')
    print(arr)
    
    import doctest
    print(doctest.testmod())