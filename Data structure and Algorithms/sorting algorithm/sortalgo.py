#bubble algorithm
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        print("i = %d"%(i+1))
        for j in range(n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)

#selection algorithm
def selectionSort(arr):
    n = len(arr)
    arr = [0] + arr
    for i in range(1, n):
        print("i = %d"%i)
        minj, minx = i, arr[i]
        for j in range(i+1, n+1):
            if arr[j] < minx:
                minj, minx = j, arr[j]
        arr[minj], arr[i] = arr[i], minx
        print(arr[1:])
    return None

#insertion algorithm
def insertionSort(arr):
    n = len(arr)
    arr = [0] + arr
    for i in range(2, n+1):
        print("i = %d"%(i-1))
        v = arr[i]
        j = i-1
        while j > 0 and arr[j] > v:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = v
        print(arr[1:])

#merge sort algorithm
def mergeSort(arr):
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
    
        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)
    
        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]
    
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
    
        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    
    def merSort(arr, p, r):
        if p < r:
            q = int((p+r)/2)
            merSort(arr, p, q)
            merSort(arr, q+1, r)
            merge(arr, p, q, r)
            print(arr)
    n = len(arr)
    merSort(arr, 0, n-1)

#quick sort algorithm
def quickSort(A):
    def Partition(A, p, r):
        x = A[r] 
        i = p - 1 
        for j in range(p, r):
            if (A[j] <= x):
                i = i +1 
                A[i], A[j] = A[j], A[i] 
        A[i+1], A[r] = A[r], A[i+1]
        print(A)
        return i+1 
    def quiSort(A, p, r):
        if len(A) == 1:
            return A
        if (p < r): 
            q = Partition(A, p, r) 
            quiSort(A, p, q-1) 
            quiSort(A, q+1, r)    
    n = len(A)
    quiSort(A, 0, n-1)

#heap sort algorithm
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
  
        # Heapify the root.
        heapify(arr, n, largest)
  
# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    print(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
        print(arr)


