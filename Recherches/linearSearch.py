def linearSearch(array,toFind):
    for i in range (len(array) - 1) :
        if(array[i] == toFind) :
            return i
    return -1