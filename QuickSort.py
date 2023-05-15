from SaveMetaData import metadata, SaveMetaData
import time
import sys

def exchange(a, b):
    return b, a


def partition(A, p, r):
    """Particiona a lista A, colocando todos os elementos menores que A[r], na esquerda"""

    x = A[r]
    i = p - 1
    trocas = comparacao = 0

    for j in range(p,r):
        if A[j] <= x:
            comparacao += 1
            i += 1
            A[i], A[j] = exchange(A[i], A[j])
            trocas += 1

    A[i + 1], A[r] = exchange(A[i + 1], A[r])
    trocas += 1
    return A, (i + 1), trocas


def quickSort(A, p, r):
    trocas = t0 = t1 = 0

    if p < r:
        A, q, trocas = partition(A, p, r)
        A, t0 = quickSort(A, p, q-1)
        A, t1 = quickSort(A, q+1, r)
    return A, (trocas+t0+t1)


if __name__ == "__main__":

    temp = str(input()).split(',')  # recebe uma string de valores inteiros separados por vírgula

    A = [int(a) for a in temp]

    dt = time.time()

    A, trocas = quickSort(A, 0, len(A)-1)

    var = metadata(tempo=(time.time() - dt), trocas = trocas)

    SaveMetaData('quickSort', var, '2023-05-11')


def QuickSort(A):
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(A)+900))
    ord, count = quickSort(A, 0, len(A)-1)
    return count


# import csv
# with open('./DATA/ordenado/asc/200000.csv') as f:
#     reader = csv.reader(f)
#     r = 0
#     for row in reader:
#         if (len(row) > 0):
#             r = row
#     print(QuickSort(A))