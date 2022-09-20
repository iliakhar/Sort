
import math

C = 0
M = 0


def SelectSort(array):
    global C, M
    max = 0
    for i in range(len(array) - 1):
        max = 0
        for j in range(len(array) - (i)):
            C += 1
            if (array[max] < array[j]):  
                max = j

        M += 3
        array[-(i+1)], array[max] = array[max], array[-(i+1)]

def BubbleSort(array):
    global C, M
    for i in range (len(array)):
        for j in range (len(array) - (i + 1)):
            C += 1
            if (array[j] > array[j + 1]):
                M += 3
                array[j], array[j + 1] = array[j + 1], array[j]

def GetPowerOfTwo(number):
    power = 0
    numToCompare = 1
    while(1):
        power += 1
        numToCompare *= 2
        if(numToCompare >= number): return power


def JoinList(array, miniListsSize):
    global C, M
    newArr = []
    secondListBeg = math.floor((math.ceil(len(array)/miniListsSize)/2))*miniListsSize
    pseudoMiniListsSize = miniListsSize
    print(" ", end = '')
    for i in range(secondListBeg):
        if(i % miniListsSize == 0 and i != 0): print("|", end = ' ')
        print(array[i], end = ' ')
    print("\n ", end = '')
    for i in range(secondListBeg, len(array)):
        if(i % miniListsSize == 0 and i != secondListBeg): print("|", end = ' ')
        print(array[i], end = ' ')

    for i in range(0, secondListBeg, miniListsSize):
        j = k =0
        if(i == secondListBeg - miniListsSize and secondListBeg*2>len(array)):
            pseudoMiniListsSize -= secondListBeg*2 - len(array)
        while(1):
            C += 1
            if(array[i+j]<array[secondListBeg + i + k]):
                newArr.append(array[i+j])
                j += 1
                M += 1
            else:
                newArr.append(array[secondListBeg + i + k])
                k += 1
                M += 1
            if(j == miniListsSize or k == pseudoMiniListsSize): break
        if(k == pseudoMiniListsSize):
            for n in range(j, miniListsSize):
                newArr.append(array[i + n])
                M += 1
        if(j == miniListsSize):
            for n in range(k, pseudoMiniListsSize):
                newArr.append(array[secondListBeg + i + n])
                M += 1
        
    if(len(array)>secondListBeg*2):
        for i in range(secondListBeg*2, len(array)):
            newArr.append(array[i])
            M += 1
        
    return newArr

def JoinList2(array, miniListsSize):
    global C, M
    newArr = []
    seriasCount = math.ceil(len(array)/miniListsSize)
    lastSeriaSize = miniListsSize - (seriasCount*miniListsSize-len(array))
    pseudoMiniListsSize = miniListsSize
    rightArrSize = math.floor(seriasCount/2)*2*miniListsSize
    print(" ", end = '')

    for i in range(0, len(array), 2*miniListsSize):
        for j in range(miniListsSize):
            if(i+j>=len(array)):break
            print(array[i + j], end = ' ')
        if(i + 2*miniListsSize < len(array)): print("|", end = ' ')

    print("\n ", end = '')

    for i in range(miniListsSize, len(array), 2*miniListsSize):
        for j in range(miniListsSize):
            if(i+j>=len(array)):break
            print(array[i + j], end = ' ')
        if(i + 2*miniListsSize < len(array)): print("|", end = ' ')

    print("\n ", end = '')
    for i in range(0, rightArrSize, 2*miniListsSize):
        j = k = 0
        if(i == rightArrSize - 2*miniListsSize and seriasCount % 2 == 0):
            pseudoMiniListsSize = lastSeriaSize
        while(1):
            C += 1
            if(array[i+j]<array[i + miniListsSize + k]):
                newArr.append(array[i+j])
                j += 1
                M += 1
            else:
                newArr.append(array[i + miniListsSize + k])
                k += 1
                M += 1
            if(j == miniListsSize or k == pseudoMiniListsSize): break
        if(k == pseudoMiniListsSize):
            for n in range(j, miniListsSize):
                newArr.append(array[i + n])
                M += 1
        if(j == miniListsSize):
            for n in range(k, pseudoMiniListsSize):
                newArr.append(array[i + miniListsSize + n])
                M += 1
    for i in range(rightArrSize, len(array)):
        newArr.append(array[i])
        
    return newArr

def MergeSort(array):
    power = GetPowerOfTwo(len(array))
    numInPower = 1
    for i in range(1, power + 1):
        print("\n Step ", i, ":")
        array = JoinList2(array, numInPower)
        print("\n Result: ", end = '')
        print(array)
        numInPower *= 2
    return array


array = [];
x = 1

print("Enter the array elements (0 for the exit):")
s =int(7/1.5)
while (0 != x):
    x = int(input())
    array.append(x)
array.remove(0)

psArr = array



C=M=0
psArr = array
print("\nMergeSort:\n")
MergeSort(psArr)
#print(psArr)
print("\n C = ", C, "  M = ", M, "  C + M = ", C + M, "\n")
