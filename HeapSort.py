import math


def HeapSort(A):
    n = len(A)
    i = math.trunc(n / 2)

    while True:
        if (i > 0):
            i -= 1
            t = A[i]
        else:
            n -= 1
            if (n <= 0):
                break

            t = A[n]
            A[n] = A[0]

        pai = i
        filho = (i*2) + 1

        while filho < n:
            if (filho + 1 < n) and (A[filho + 1] > A[filho]):
                filho += 1

            if (A[filho] > t):
                A[pai] = A[filho]

                pai = filho
                filho = pai * 2 + 1
            else:
                break

        A[pai] = t

    print(A)


HeapSort([5, 58, 46, 59, 5, 5184, 54, 7, 0, 447, 58, 1])
