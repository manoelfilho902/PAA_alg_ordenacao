MinMerge = 64

changes = 0


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
                Merge(A, left, mind, rigth)
        size = 2 * size

    return changes
    # m = main()
    # m.IsSorted(A)
    # with open('./log/tim.csv', 'w', encoding='UTF-8') as f:
    #     w = csv.writer(f)
    #     w.writerow(A)


def Merge(A, l, m, r):
    len1 = m - l + 1
    len2 = r - m
    left = []
    rigth = []
    global changes

    ret = 0

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
        changes += 1
        ret +=1

        k += 1

    while i < len1:
        A[k] = left[i]
        k += 1
        i += 1
        changes += 1
        ret +=1

    while j < len2:
        A[k] = rigth[j]
        k += 1
        j += 1
        changes += 1
        ret +=1
 
    return ret

def minRunLength(n):
    r = 0
    while (n >= MinMerge):
        r |= n & 1
        n >>= 1

    return n + r


def InsertionSort(A, left, right):
    global changes
    for i in range(left + 1, right + 1):
        j = i
        while j > left and A[j] < A[j-1]:
            aux = A[j]
            A[j] = A[j-1]
            A[j-1] = aux
            j -= 1
            changes += 1


# TimSort([5, 58, 46, 59, 5, 5184, 54, 7,00,447,58,1])


# with open('./aleatorio/700000.csv', 'r') as f:
#     reader = csv.reader(f)
#     r = 0
#     for row in reader:
#         if (len(row) > 0):
#             r = row
#     TimSort(r)
