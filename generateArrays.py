import random

def generateArrays(powerOfTwo) :

    arraySizes = []
    generatedArrays = []

    for i in range (powerOfTwo) :
        arraySizes.append(pow(10, i+1))
        generatedArrays.append([])

    for i in range (powerOfTwo) : 
        for j in range (arraySizes[i]) : 
            generatedArrays[i].append(random.randrange(1, 100))
    return generatedArrays