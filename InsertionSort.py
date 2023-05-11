def InsertionSort(A):
    contador = 0
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        print(j, i)
        while(i>=0 and A[i]>key):
            aux = A[i+1]
            A[i+1] = A[i]
            A[i] = aux
            contador += 1
            i -= 1

        A[i+1] = key
    print(A)
    return contador

