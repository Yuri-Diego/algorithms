# Implementacao do QuickSort, Algoritmo de ordenacao com a estategia: dividir e conquistar.
# Melhor caso (Best case): O(n log n).
# Pior caso (Worst case): O(n^2).

def quickSort(arr, left, right):
    if left < right:
        print(arr[left:right+1])
        pi = partition(arr, left, right)
        quickSort(arr, left, pi-1)
        quickSort(arr, pi + 1, right)

def partition(arr, left, right):
    pivot = arr[right]

    i = left-1

    for j in range(left,right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

arr = [0,3,6,7,8,4,2,1,5]

quickSort(arr, 0, len(arr)-1)