# Radix sort based on count sort
# Author: Y.

def count_sort(arr, place):
    count = [0] * 10
    output = [0] * len(arr)

    # Record count
    for i in range(len(arr)):
        index = arr[i] // place
        count[index % 10] += 1
    
    # Recode index of each elem for output
    for i in range(1, 10):
        count[i] += count[i-1]

    i = len(arr) - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    for i in range(len(arr)):
        arr[i] = output[i]
    
    return


def radix_sort(arr):

    max_val = max(arr)
    place = 1

    while max_val // place > 0:
        count_sort(arr, place)
        place *= 10
        

if __name__=="__main__":
    
    arr = [121, 432, 564, 23, 1, 45, 788]
    radix_sort(arr)
    print(arr)