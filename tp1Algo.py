import random
import time

# Fonctions importées
from generateArrays import generateArrays
from Recherches.linearSearch import linearSearch
from Tris.selectionSort import selectionSort
from Tris.quickSort import quickSortStart
from Tris.mergeSort import mergeSort
from Tris.triabulle import triaBulle
from Tris.triinsertion import triinsertion
from Tris.trihollandais import trihollandais
from Recherches.recherchedichotomique import recherche_dichotomique

# Nombre de tableaux à générer
arraysNumber = 4

# Tableau conclusion
conclusionArray = []

# Demande à l'utilisateur s'il veut afficher les tableaux avant et après les opérations
print("Do you want to print the before/after arrays and the results of the searches? (y/n)")
printArrays = ''
while(printArrays != 'y' and printArrays != 'n') :
    printArrays = input()

def searchArray(searchFunction, name) : 
    arrays = generateArrays(arraysNumber)
    execTimes = []
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
        print(f"Temps d'éxecution : {result[0]} microsecondes")
        print('---------------------------------')
        execTimes.append(result[0])
    print('')
    print('')
    reportObj = {'name' : name, 'execTimes' : execTimes}
    conclusionArray.append(reportObj)

def sortArray(sortingFunction, name) : 
    arrays = generateArrays(arraysNumber)
    execTimes = []
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
        print(f"Temps d'éxecution : {result[0]} microsecondes")
        print('---------------------------------')
        execTimes.append(result[0])
    print('')
    print('')
    reportObj = {'name' : name, 'execTimes' : execTimes}
    conclusionArray.append(reportObj)

def mesurer_temps_execution (fonction, *args) :
    debut = time.perf_counter()
    result = fonction(*args)
    fin = time.perf_counter()
    return [round(((fin - debut) * 1000000), 3), result]

def translate(array) :
    dutchArray = []
    for i in range(len(array)) : 
        dutchArray.append(array[i]%3)
    return dutchArray

def printConclusion(array, sizes):
    
    headers = ['Temps exprimés en µs']
    data = []
    col_widths = []

    for i in range(sizes) : 
        headers.append(f'Nombre d\'éléments : {pow(10, i+1)}')

    for i in range(len(array)) :
        array[i]['execTimes'].insert(0, array[i]['name'])
        data.append(array[i]['execTimes'])

    for i in range(sizes + 1) : 
        col_widths.append(25)

    separator = "-" * (sum(col_widths) + len(col_widths) * 3 + 1)

    # Format a single row
    def format_row(row):
        return "|" + "|".join(f" {str(item).ljust(width)} " for item, width in zip(row, col_widths)) + "|"
    
    # Print the table
    print(separator)
    print(format_row(headers))  # Header row
    print(separator)
    for row in data:
        print(format_row(row))  # Data rows
    print(separator)

# Appel des fonctions de recherche et de tri
searchArray(linearSearch, "Recherche linéaire")
searchArray(recherche_dichotomique, "Recherche dichotomique")
sortArray(selectionSort, "Tri par sélection")
sortArray(quickSortStart, "Tri rapide")
sortArray(triaBulle, "Tri à bulle")
sortArray(triinsertion, "Tri par insertion")
sortArray(trihollandais, "Tri hollandais")
sortArray(mergeSort, "Tri fusion")

printConclusion(conclusionArray, arraysNumber)