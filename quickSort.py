def partitioning(array, first, last, pivot) :
    count = first
    array[last], array[pivot] = array[pivot], array[last]
    for i in range(first, last) : 
        if array[i] <= array[last] :
            array[i], array[count] = array[count], array[i]
            count += 1
    array[last], array[count] = array[count], array[last]
    return count

def quickSort(array, first, last) :
    if first < last : 
        pivot = first
        pivot = partitioning(array, first, last, pivot)
        quickSort(array, first, pivot-1)
        quickSort(array, pivot+1, last)

def quickSortStart(array) : 
    quickSort(array, 0, len(array) - 1)
    return array