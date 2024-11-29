def mergeSort(array) :
    if len(array) <= 1 :
        return array
    else : 
        return merge(mergeSort(array[:len(array)//2]), mergeSort(array[len(array)//2:]))
    
def merge(array1, array2) : 
    arrayReturn = []
    while len(array1) > 0 or len(array2) > 0 :
        if len(array1) == 0:
            arrayReturn.append(array2[0])
            array2.pop(0)
        elif len(array2) == 0 :
            arrayReturn.append(array1[0])
            array1.pop(0)
        elif array1[0] <= array2[0] :
            arrayReturn.append(array1[0])
            array1.pop(0)
        else :
            arrayReturn.append(array2[0])
            array2.pop(0)
    return arrayReturn