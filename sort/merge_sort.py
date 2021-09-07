# Merge sort using Divide and Conquer
# Author: Y.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    return merge(left_arr, right_arr)



def merge(left_arr, right_arr):
    i, j = 0, 0
    sorted = []

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            sorted.append(left_arr[i])
            i += 1
        else:
            sorted.append(right_arr[j])
            j += 1
    sorted = sorted + left_arr[i:] + right_arr[j:]
    
    return sorted


if __name__=="__main__":

    arr = [6, 1, 0, -2, -4, 0, 3, 10]
    res = merge_sort(arr)
    print(res)
