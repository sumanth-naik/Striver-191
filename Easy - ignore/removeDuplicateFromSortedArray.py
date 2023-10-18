

def removeDuplicatesFromSortedArray(arr, n):
    i,j = 0, 0
    while j<n:
        if arr[i]==arr[j]:
            j += 1
        else:
            i += 1
            arr[i] = arr[j]
            j += 1
    return i+1