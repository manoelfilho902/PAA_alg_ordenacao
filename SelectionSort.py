from SaveMetaData import metadata, SaveMetaData
import time

def SelectionSort(A):
    contador = 0
    for i in range(len(A)-1):
        menor = i
        for j in range(i+1, len(A)):
            if (A[j] < A[menor]):
                menor = j
      
        if (A[i] != A[menor]):
            aux = A[i]
            A[i] = A[menor]
            A[menor] = aux
            contador += 1
    return contador
