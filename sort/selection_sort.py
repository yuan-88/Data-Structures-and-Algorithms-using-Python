# Selection sort
# Author: Y.

def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


if __name__=="__main__":

    arr = [6, 1, 0, -2, -4, 3, 10]
    selection_sort(arr)
    print(arr)