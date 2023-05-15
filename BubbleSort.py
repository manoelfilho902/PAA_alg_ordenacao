def BubbleSort(A):
    contador = 0
    count = True
    while (True):
        changed = False
        for i in range(len(A)-1):
            # print(A[i], A[i+1])
            if (A[i] > A[i+1]):
                aux = A[i]
                A[i] = A[i+1]
                A[i+1] = aux
                changed = True
                contador += 1         
        if(not changed):
            break
    return contador