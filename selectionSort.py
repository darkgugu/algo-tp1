def selectionSort(array) : 
    for i in range (len(array)) :
        lowestIndex = i 
        for j in range (i, len(array)) : 
            if(array[j] < array[lowestIndex]) : 
                lowestIndex = j
        array[i], array[lowestIndex] = array[lowestIndex], array[i]
    return array