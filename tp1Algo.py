from generateArrays import generateArrays
from linearSearch import linearSearch
from selectionSort import selectionSort
from quickSort import quickSortStart
import random
import time

arraysNumber = 4

print("Do you want to print the before and after arrays ? (y/n)")
printArrays = ''
while(printArrays != 'y' and printArrays != 'n') :
    printArrays = input()

def searchArray(searchFunction, name) : 
    arrays = generateArrays(arraysNumber)
    print(f'#### {name} ####')
    for i in range (arraysNumber) :
        numberToFind = random.randrange(1, 100)
        if(printArrays != 'n') :
            print(f'Tableau {i+1} ({len(arrays[i])} éléments) :')
            print(f'Nombre à trouver : {numberToFind}')
            print(arrays[i])
            indexToFInd = (searchFunction(arrays[i], numberToFind))
            if (indexToFInd != -1) :
                print(f'Index de numéro à trouver (premier occurence) : {indexToFInd}')
            else : 
                print('Nombre non trouvé dans le tableau')
        print('---------------------------------')

def sortArray(sortingFunction, name) : 
    arrays = generateArrays(arraysNumber)
    print(f'#### {name} ####')
    for i in range(arraysNumber) :
        print(f'Tableau {i+1} ({len(arrays[i])} éléments) :')
        if(printArrays != 'n') :
            print('Tableau non trié : ')
            print(arrays[i])
            print('Tableau trié : ')
            print(mesurer_temps_execution(sortingFunction, arrays[i])[1])
        print(f"Temps d'éxecution : {mesurer_temps_execution(sortingFunction, arrays[i])[0]}")
        print('---------------------------------')

def mesurer_temps_execution (fonction, *args) :
    debut = time.time()
    result = fonction(*args)
    fin = time.time()
    return [fin - debut, result]

searchArray(linearSearch, "Recherche linéaire")
sortArray(selectionSort, "Tri par sélection")
sortArray(quickSortStart, "Tri rapide")