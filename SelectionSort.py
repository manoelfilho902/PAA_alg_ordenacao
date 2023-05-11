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
 

dt = time.time()

troca = SelectionSort([515,48,2,4,8,8])
    
var = metadata(tempo=(time.time() - dt), trocas = troca)

SaveMetaData('SelectionSort', var, '2023-05-11')