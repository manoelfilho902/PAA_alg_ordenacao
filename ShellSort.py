import csv


def ShellSort(A):
    h = 1
    n = len(A)
    count = 0

    while h > 0:
        for i in range(h, n):
            c = A[i]
            j = i
            while j >= h and c > A[j-h]:
                A[j] = A[j - h]
                j = j - h
                count += 1
                A[j] = c

        h = int(h/2)

    return count


# with open('./DATA/ordenado/desc/1000.csv', 'r') as f:
#     reader = csv.reader(f)
#     r = 0
#     for row in reader:
#         if (len(row) > 0):
#             r = row

#     print(ShellSort(r))
