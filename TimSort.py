import math
MinMerge = 32


def TimSort(A):
    n = len(A)
    minRun = minRunLength(n)

    for i in range(0, n, minRun):
        InsertionSort(A, i, min(i + minRun - 1, n-1))

    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mind = min(left + size - 1, n - 1)
            rigth = min(left + 2 * size - 1, n - 1)

            if (mind < rigth):
                merge(A, left, mind, rigth)
        size *= 2

    print(A)


def merge(A, l, m, r):
    len1 = m - l + 1
    len2 = r-m
    left = []
    rigth = []

    for i in range(len1):
        left.append(A[l + i])

    for i in range(len2):
        rigth.append(A[m + 1 + i])

    i = 0
    j = 0
    k = l

    while i < len1 and j < len2:
        if (left[i] <= rigth[j]):
            A[k] = left[i]
            i += 1
        else:
            A[k] = rigth[j]
            j += 1

        k += 1

    while i < len1:
        A[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        A[k] = left[j]
        k += 1
        j += 1


def minRunLength(n):
    if (n >= 0):
        r = 0

        while (n >= MinMerge):
            r |= (n & 1)
            n >>= 11

    return n + r


def InsertionSort(A, left, right):
    for i in range(left+1, right+1):
        temp = A[i]
        j = i-1

        while j >= left and A[j] > temp:
            aux = A[j]
            A[j] = A[j+1]
            A[j+1] = aux
            j -= 1

        A[j+1] = temp


TimSort([5, 58, 46, 59, 5, 5184, 54, 7,00,447,58,1])
