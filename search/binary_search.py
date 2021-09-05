# Binary search
# Author: Y.

# Simple Binary Search
def binary_search(arr, val):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if val > arr[mid]:
            left = mid + 1
        elif val < arr[mid]:
            right = mid - 1
        else:
            return mid
    return -1

# Insertion by binary search
def search_insert(arr, val):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if val > arr[mid]:
            left = mid + 1
        elif val < arr[mid]:
            right = mid - 1
        else:
            return mid
    return right + 1


if __name__ == "__main__":
    
    arr = [-1,0,3,5,9,12]
    target = 9
    print(f"result: {binary_search(arr, target)}")
    print(f"answer: 4")

    arr = [-1,0,3,5,9,12]
    target = 2
    print(f"result: {binary_search(arr, target)}")
    print(f"answer: -1")

    arr = [1, 3, 5, 6]
    target = 4
    idx = search_insert(arr, target)
    arr.insert(idx, target)
    print(f"result: {arr}")