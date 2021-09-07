# Bucket sort based on time sort
# Author: Y.

def bucket_sort(arr):
    buckets = []
    for i in range(len(arr)):
        buckets.append([])

    # Insert element into their respective bucket
    for elem in arr:
        index = int(elem * 10)
        buckets[index].append(elem)
    
    # Sort the elements of each bucket
    for bucket in buckets:
        bucket.sort()
    
    # Combine the sorted elements
    k = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1


if __name__=="__main__":

    arr = [.42, .32, .33, .52, .37, .47, .51]
    bucket_sort(arr)
    print(arr)

