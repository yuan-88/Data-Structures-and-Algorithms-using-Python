# Shell sort
# Author: Y.

def shell_sort(arr):
    interval = len(arr) // 2
    while interval > 0:
        for pivot in range(interval, len(arr)):
            temp = arr[pivot]
            j = pivot
            while j >= interval and arr[j-interval] > temp:
                arr[j] = arr[j-interval]
                j -= interval
            arr[j] = temp
        interval = interval // 2


if __name__=="__main__":
    
    arr = [6, 1, 0, -2, -4, 3, 10]
    shell_sort(arr)
    print(arr)