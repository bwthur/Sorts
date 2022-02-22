import random
import memory_profiler
from time_profiler import timer

def genElements(minVal, maxVal, amount):

    #Generate list of unique random numbers
    try:
        eleList = random.sample(range(minVal, maxVal), amount)
    except ValueError:
        print("Not enough numbers to complete range.")

    return eleList

@timer()
# @profile
def selectionSort(sortArray):
    sortedArray = []
    for i in range(len(sortArray)):
        minimumValPos = sortArray.index(min(sortArray))
        removedVal = sortArray.pop(minimumValPos)
        sortedArray.append(removedVal)
    sortArray = sortedArray
    return (sortArray)

@timer()
# @profile
def insertionSort(sortArray):
    for i in range(len(sortArray)):
        while sortArray[i-1] is not None and sortArray[i-1] > sortArray[i]:
            j = sortArray[i]
            k = sortArray[i-1]
            sortArray.insert(i, k)
            sortArray.insert(i-1, j)
        return sortArray

@timer()
# @profile
def bubbleSort(sortArray):
    arrayLen = len(sortArray)
    for i in range(arrayLen):
        for j in range(0, arrayLen-i-1):
            if sortArray[j] > sortArray[j+1]:
                sortArray[j], sortArray[j+1] = sortArray[j+1], sortArray[j]
    return sortArray

testArr = genElements(1, 100001, 100000)
# print("Insertion: ", insertionSort(testArr))
print("Selection: ", selectionSort(testArr))
# print("Bubble : ", bubbleSort(testArr))