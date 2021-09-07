# Quick sort using Divide and Conquer
# Author: Y.


def quick_sort(arr, left, right):
    if left >= right:
        return
    
    l, r, pivot = left, right, left
    while l < r:
        # If right value is greater than pivot,
        # and left value is less than pivot, swap left and right
        while arr[r] > arr[pivot] and l < r:
            r -= 1
        while arr[l] <= arr[pivot] and l < r:
            l += 1
        arr[l], arr[r] = arr[r], arr[l]
    
    # Swap final left value and pivot
    arr[pivot], arr[l] = arr[l], arr[pivot]
    
    # Update pivot, left, right and repeat the above steps
    pivot = l    
    quick_sort(arr, left, pivot-1)
    quick_sort(arr, pivot+1, right)


if __name__=="__main__":

    arr = [6, 1, 0, -2, -4, 0, 3, 10]
    print(arr)
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
