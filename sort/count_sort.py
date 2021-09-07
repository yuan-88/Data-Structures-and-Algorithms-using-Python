# Count sort
# Author: Y.

def count_sort(arr):
    max_val, min_val = max(arr), min(arr)
    gap = max_val - min_val + 1
    count = [0] * gap

    for elem in arr:
        count[elem-min_val] += 1
    
    output = []
    for i, cnt in enumerate(count):
        elem = i + min_val
        output += [elem] * cnt
    
    for i in range(len(arr)):
        arr[i] = output[i]


if __name__=="__main__":

    arr = [6, 1, 0, -2, -4, 0, 3, 10]
    count_sort(arr)
    print(arr)