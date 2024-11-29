import random
import time

# Fonctions importées
from generateArrays import generateArrays
from linearSearch import linearSearch
from selectionSort import selectionSort
from quickSort import quickSortStart
from mergeSort import mergeSort
from triabulle import triaBulle
from triinsertion import triinsertion
from trihollandais import trihollandais
from recherchedichotomique import recherche_dichotomique

# Nombre de tableaux à générer
arraysNumber = 1

# Demande à l'utilisateur s'il veut afficher les tableaux avant et après les opérations
print("Do you want to print the before/after arrays and the results of the searches? (y/n)")
printArrays = ''
while(printArrays != 'y' and printArrays != 'n') :
    printArrays = input()

def searchArray(searchFunction, name) : 
    arrays = generateArrays(arraysNumber)
    print(f'#### {name} ####')
    for i in range (arraysNumber) :
        numberToFind = random.randrange(1, 100)
        print(f'Tableau {i+1} ({len(arrays[i])} éléments) :')
        result = mesurer_temps_execution(searchFunction, arrays[i], numberToFind)
        if(printArrays != 'n') :
            print(f'Nombre à trouver : {numberToFind}')
            print(arrays[i])
            indexToFInd = result[1]
            if (indexToFInd != -1) :
                print(f'Index de numéro à trouver (premier occurence) : {indexToFInd}')
            else : 
                print('Nombre non trouvé dans le tableau')
        print(f"Temps d'éxecution : {result[0]} secondes")
        print('---------------------------------')

def sortArray(sortingFunction, name) : 
    arrays = generateArrays(arraysNumber)
    print(f'#### {name} ####')
    for i in range(arraysNumber) :
        if name == "Tri hollandais" : 
            arrays[i] = translate(arrays[i])
        print(f'Tableau {i+1} ({len(arrays[i])} éléments) :')
        displayArray = arrays[i].copy()
        result = mesurer_temps_execution(sortingFunction, arrays[i])
        if(printArrays != 'n') :
            print('Tableau non trié : ')
            print(displayArray)
            print('Tableau trié : ')
            print(result[1])
        print(f"Temps d'éxecution : {result[0]} secondes")
        print('---------------------------------')

def mesurer_temps_execution (fonction, *args) :
    debut = time.time()
    result = fonction(*args)
    fin = time.time()
    return [fin - debut, result]

def translate(array) :
    dutchArray = []
    for i in range(len(array)) : 
        dutchArray.append(array[i]%3)
    return dutchArray

# Appel des fonctions de recherche et de tri
searchArray(linearSearch, "Recherche linéaire")
searchArray(recherche_dichotomique, "Recherche dichotomique")
sortArray(selectionSort, "Tri par sélection")
sortArray(quickSortStart, "Tri rapide")
sortArray(triaBulle, "Tri à bulle")
sortArray(triinsertion, "Tri par insertion")
sortArray(trihollandais, "Tri hollandais")
sortArray(mergeSort, "Tri fusion")