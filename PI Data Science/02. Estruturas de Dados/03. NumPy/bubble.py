import numpy as np

def bubbleSort(lista, n=None):
    n = len(lista) if n is None else n
    if (n < 1):
        return
    swapped = False
    for k in range(n-1):
        if (lista[k] > lista[k+1]):
            lista[k], lista[k+1] = lista[k+1], lista[k]
            swapped = True
    if __debug__:
        print(n)
    if swapped is True:
        bubbleSort(lista, n-1)


arr = [17, 26, 54, 93, 77, 31, 44, 55, 20]
bubbleSort(arr)
print(arr)

import numpy as np
arr = [17, 26, 54, 93, 77, 31, 44, 55, 20]
ar = np.array(arr)
ar = np.sort(ar, kind='quicksort')
print(ar)

