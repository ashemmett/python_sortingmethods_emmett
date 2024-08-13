#ashton_emmett_ds2 #10564416 (task 3) 2023 

import random
import time

#functions

#def testSelection
def selectionSort(array):
    starttime = time.time()
    Ncompare = 0
    i=0
    while i<len(array)-1:     
        minIndex=i           
        j=i+1
        while j<len(array):    
            if array[j]<array[minIndex]:
                Ncompare += 1
                minIndex = j
            j += 1
        if minIndex != i:
            Sswap(array, minIndex, i)
        i += 1    
    endtime = time.time()
    runtime = (endtime - starttime)*1000
    return array, Ncompare, runtime 

def Sswap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

#def testInsertion
def insertionSort(array):
    starttime = time.time()
    Ncompare = 0
    i=1                               
    while i<len(array):                
        itemToInsert = array[i]  
        j=i-1
        while j>=0:                  
            if itemToInsert <array[j]:
                Ncompare += 1
                array[j+1] = array[j]   
                j -= 1
            else:
                break                 
        array[j+1]= itemToInsert       
        i += 1
    endtime = time.time()
    runtime = (endtime - starttime)*1000
    return array, Ncompare, runtime 
   

#def testMerge
def mergeSort(array):
    starttime = time.time()
    Ncompare = [0]
    copyBuffer = [None]*(len(array))
    mergeSortHelper(array, copyBuffer, 0, len(array)-1, Ncompare)
    endtime = time.time()
    runtime = (endtime - starttime)*1000
    return array, Ncompare[0], runtime 

def mergeSortHelper(array, copyBuffer, low, high, Ncompare):
    if low <high:
        middle = (low+high)//2
        mergeSortHelper(array, copyBuffer, low, middle, Ncompare)
        mergeSortHelper(array, copyBuffer, middle+1, high, Ncompare)
        merge(array, copyBuffer, low, middle, high, Ncompare)
    return 

def merge(array, copyBuffer, low, middle, high, Ncompare):
    i1=low
    i2=middle+1
    for i in range(low, high+1):
        if i1>middle:
            copyBuffer[i]=array[i2] 
            i2 +=1
        elif i2>high:
            copyBuffer[i] = array[i1] 
            i1 +=1
        elif array[i1]<array[i2]:
            Ncompare[0] += 1
            copyBuffer[i] = array[i1] 
            i1 +=1            
        else:                
            Ncompare[0] += 1
            copyBuffer[i] = array[i2] 
            i2 +=1
    for i in range(low, high+1):        
        array[i] = copyBuffer[i]      
    return 


#def testQuick
def quickSort(array):
    starttime = time.time()
    Ncompare = [0]
    quicksortHelper(array, 0, len(array) - 1, Ncompare)
    endtime = time.time()
    runtime = (endtime - starttime)*1000
    return array, Ncompare[0], runtime

def quicksortHelper(array, left, right, Ncompare):
    if left < right:
        pivotLocation = partition(array, left, right, Ncompare)
        quicksortHelper(array, left, pivotLocation - 1, Ncompare)
        quicksortHelper(array, pivotLocation + 1, right, Ncompare)

def partition(array, left, right, Ncompare):
    middle = (left + right) // 2
    pivot = array[middle]
    array[middle] = array[right]
    array[right] = pivot 
    boundary = left
    for index in range(left, right):
        Ncompare[0] += 1
        if array[index] < pivot:
            Qswap(array, index, boundary)
            boundary += 1
    Qswap (array, right, boundary)
    return boundary

def Qswap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


#def testHeap
def Heap(array, length, index, Ncompare):
    larger_index = index
    l_child = 2 * larger_index + 1
    r_child = 2 * larger_index + 2
    
    if l_child < length and array[larger_index] < array[l_child]:
        Ncompare[0] += 1
        larger_index = l_child
    
    if r_child < length and array[larger_index] < array[r_child]:
        Ncompare[0] += 1
        larger_index = r_child

    if larger_index != index:
        array[index], array[larger_index] = array[larger_index], array[index]

        Heap(array, length, larger_index, Ncompare)

def heapSort(array):
    starttime = time.time()
    Ncompare = [0]
    for i in range(len(array)-1, -1, -1):
        Heap(array, len(array), i, Ncompare)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        Heap(array, i, 0, Ncompare)
    endtime = time.time()
    runtime = (endtime - starttime)*1000
    return array, Ncompare[0], runtime    

#def testBubble
def BS(array):
    starttime = time.time()
    n = len(array)
    Ncompare = 0
    for i in range(n-1):
        for j in range(n-1):
            Ncompare += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    endtime = time.time()
    runtime = (endtime - starttime)*1000
    return array, Ncompare, runtime
    

#def testObs1
def Obs1(array):
    starttime = time.time()
    n = len(array)
    Ncompare = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                Ncompare += 1
    endtime = time.time()
    runtime = (endtime - starttime)*1000            
    return array, Ncompare, runtime

#def testObs2
def Obs2(array):
    starttime = time.time()
    n = len(array)
    Ncompare = 0
    flagswap = False
    while not flagswap:
        flagswap = True
    for i in range(n-1):
        for j in range(n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                Ncompare += 1
                flagswap = False
    n = n-1
    endtime = time.time()
    runtime = (endtime - starttime)*1000                    
    return array, Ncompare, runtime

#def testObs3():
def Obs3(array):
    starttime = time.time()
    n = len(array)
    Ncompare = 0
    flagswap = False
    while not flagswap:
        flagswap = True
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                Ncompare += 1
                flagswap = False
    n = n-1
    endtime = time.time()
    runtime = (endtime - starttime)*1000                    
    return array, Ncompare, runtime

#def testSinkdown():
def SDS(array):
    starttime = time.time()
    n = len(array)
    Ncompare = 0
    for i in range(n-1):
        for j in (range(n-1, 0, -1)):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                Ncompare += 1
    endtime = time.time()
    runtime = (endtime - starttime)*1000             
    return array, Ncompare, runtime

#def testbidirectional():
def BDBS(array):
    starttime = time.time()
    n = len(array)
    Ncompare = [0]
    for i in range(n-1):
        for j in range(n-1): #left to right scan
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                Ncompare[0] += 1
        for j in (range(n-1, 0, -1)): #right to left scan
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]   
                Ncompare[0] += 1     
    endtime = time.time()
    runtime = (endtime - starttime)*1000             
    return array, Ncompare, runtime


#main
end = False
while not end:
    print('---------------------------------------------------------------------------------')  
    print('Algorithm Analysis Program')
    print('\n') 
    print('1. Test an individual sorting algorithm')   
    print('2. Test multiple sorting algorithms')
    print('3. Exit')
    print('\n')         
    menu=input('Enter an option (1-3):')
    print('----------------------------------------') 
#quit program
    if menu =='3':
          end == True
          print('Goodbye!')
          print('----------------------------------------')
#part 1          
    elif menu =='1':
        print('1. Test selection sort algorithm')
        print('2. Test insertion sort algorithm')
        print('3. Test merge sort algorithm')
        print('4. Test quick sort algorithm')
        print('5. Test heap sort algorithm')
        print('6. Test bubble sort algorithm')
        print('7. Test Obs1-bubble sort algorithm')
        print('8. Test Obs2-bubble sort algorithm')
        print('9. Test Obs3-bubble sort algorithm')
        print('10. Test Sink-down sort algorithm')
        print('11. Test Bi-directional sort algorithm')
        option=input('Choose an option (1-11): ').lower()   
        print('----------------------------------------') 
        
        if option == '1':
            print("Selection-Sort")
            size = int(input("Please enter a size for the randomised array: " ))
            lyst = []
            for count in range(size):
                lyst.append(random.randint(1, size*5+1))
            array, Ncompare, runtime = selectionSort(lyst)
            print(array)
            print("Number of comparisons:", Ncompare)
            print("Runtime (in ms):", runtime)

        if option == '2':
            print("Insertion-Sort")
            size = int(input("Please enter a size for the randomised array: " ))
            lyst = []
            for count in range(size):
                lyst.append(random.randint(1, size*5+1))
            array, Ncompare, runtime = insertionSort(lyst)
            print(array)
            print("Number of comparisons:", Ncompare)
            print("Runtime (in ms):", runtime)

        if option == '3':
            print("Merge-Sort")
            size = int(input("Please enter a size for the randomised array: " ))
            lyst = []
            for count in range(size):
                lyst.append(random.randint(1, size*5+1))
            array, Ncompare, runtime = mergeSort(lyst)
            print(array)
            print("Number of comparisons:", Ncompare)
            print("Runtime (in ms):", runtime)

        if option == '4':
            print("Quick-Sort")
            size = int(input("Please enter a size for the randomised array: " ))
            lyst = []
            for count in range(size):
                lyst.append(random.randint(1, size*5+1))
            array, Ncompare, runtime = quickSort(lyst)
            print(array)
            print("Number of comparisons:", Ncompare)
            print("Runtime (in ms):", runtime)

        if option == '5':
            print("Heap-Sort")
            size = int(input("Please enter a size for the randomised array: " ))
            lyst = []
            for count in range(size):
                lyst.append(random.randint(1, size*5+1))
            array, Ncompare, runtime = heapSort(lyst)
            print(array)
            print("Number of comparisons:", Ncompare)
            print("Runtime (in ms):", runtime)
        
        elif option == '6':
            print("Bubble-Sort")
            size = int(input("Please enter a size for the randomised array: " ))
            lyst = []
            for count in range(size):
                lyst.append(random.randint(1, size*5+1))
            array, Ncompare, runtime = BS(lyst)
            print(array)
            print("Number of comparisons:", Ncompare)
            print("Runtime (in ms):", runtime)
            
        elif option == '7':
            print("Obs1")
            size = int(input("Please enter a size for the randomised array: " ))
            lyst = []
            for count in range(size):
                lyst.append(random.randint(1, size*5+1))
            array, Ncompare, runtime = Obs1(lyst)
            print(array)
            print("Number of comparisons:", Ncompare)
            print("Runtime (in ms):", runtime)
            
        elif option == '8':
            print("Obs2")
            size = int(input("Please enter a size for the randomised array: " ))
            lyst = []
            for count in range(size):
                lyst.append(random.randint(1, size*5+1))
            array, Ncompare, runtime = Obs2(lyst)
            print(array)
            print("Number of comparisons:", Ncompare)
            print("Runtime (in ms):", runtime)
            
        elif option == '9':
            print("Obs3")
            size = int(input("Please enter a size for the randomised array: " ))
            lyst = []
            for count in range(size):
                lyst.append(random.randint(1, size*5+1))
            array, Ncompare, runtime = Obs3(lyst)
            print(array)
            print("Number of comparisons:", Ncompare)
            print("Runtime (in ms):", runtime)

        elif option == '10':
            print("Sink-Down-Sort")
            size = int(input("Please enter a size for the randomised array: " ))
            lyst = []
            for count in range(size):
                lyst.append(random.randint(1, size*5+1))
            array, Ncompare, runtime = SDS(lyst)
            print(array)
            print("Number of comparisons:", Ncompare)
            print("Runtime (in ms):", runtime)

        elif option == '11':
            print("Bidirectional-Bubble-Sort")
            size = int(input("Please enter a size for the randomised array: " ))
            lyst = []
            for count in range(size):
                lyst.append(random.randint(1, size*5+1))
            array, Ncompare, runtime = BDBS(lyst)
            print(array)
            print("Number of comparisons:", Ncompare)
            print("Runtime (in ms):", runtime)



#part 2
    elif menu =='2':
        size = int(input("Please enter a size for the randomised array: " ))
        print('| Sorting algorithm name | Array size | Num. of Comparisons | Run time (in ms.) |')
        print('---------------------------------------------------------------------------------')     
        lyst = []
        for count in range(size):
            lyst.append(random.randint(1, size*5+1))

        array, Ncompare, runtime = selectionSort(lyst)
        print("1.Selection-Sort:            ", size, "          ", Ncompare, "               ", runtime, "ms")
        
        array, Ncompare, runtime = insertionSort(lyst)
        print("2.Insertion-Sort:            ", size, "          ", Ncompare, "               ", runtime, "ms")
        
        array, Ncompare, runtime = mergeSort(lyst)
        print("3.Merge-Sort:                ", size, "          ", Ncompare, "               ", runtime, "ms")
        
        array, Ncompare, runtime = quickSort(lyst)
        print("4.Quick-Sort:                ", size, "          ", Ncompare, "               ", runtime, "ms")
        
        array, Ncompare, runtime = heapSort(lyst)
        print("5.Heap-Sort:                 ", size, "          ", Ncompare, "               ", runtime, "ms")

        array, Ncompare, runtime = BS(lyst)
        print("6.Bubble-Sort:               ", size, "          ", Ncompare, "               ", runtime, "ms")
        
        array, Ncompare, runtime = Obs1(lyst)
        print("7.Obs1:                      ", size, "          ", Ncompare, "               ", runtime, "ms")
        
        array, Ncompare, runtime = Obs2(lyst)
        print("8.Obs2:                      ", size, "          ", Ncompare, "               ", runtime, "ms")
        
        array, Ncompare, runtime = Obs3(lyst)
        print("9.Obs3:                      ", size, "          ", Ncompare, "               ", runtime, "ms")
        
        array, Ncompare, runtime = SDS(lyst)
        print("10.Sink-Down-Sort:            ", size, "          ", Ncompare, "               ", runtime, "ms")
        
        array, Ncompare, runtime = BDBS(lyst)
        print("11.Bi-Directional-Bubble-Sort:", size, "          ", Ncompare, "               ", runtime, "ms")

