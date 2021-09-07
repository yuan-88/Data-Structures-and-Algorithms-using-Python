# Insertion sort
# Author: Y.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and tmp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp


if __name__=="__main__":

    arr = [6, 1, 0, -2, -4, 3, 10]
    insertion_sort(arr)
    print(arr)
    