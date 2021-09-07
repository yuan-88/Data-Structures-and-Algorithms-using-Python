# Bubble sort
# Author: Y.

def bubble_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            break



if __name__=="__main__":

    arr = [6, 1, 0, -2, -4, 3, 10]
    bubble_sort(arr)
    print(arr)
