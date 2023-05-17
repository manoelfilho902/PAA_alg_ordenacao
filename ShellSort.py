def ShellSort(A):
    h = 1
    n = len(A)

    count = 0

    while h < n:
        h = h * 3 + 1

    h = int(h / 3)

    while h > 0:
        for i in range(h, n):
            c = A[i]
            j = i

            while j >= h and A[j-h] > c:
                A[j] = A[j - h]
                j -= j - h
                count += 1
            A[j] = c

        h = int(h/2)
    return count

# import csv

# with open('./DATA/ordenado/asc/1000.csv', 'r') as f:
#     reader = csv.reader(f)
#     r = 0
#     for row in reader:
#         if (len(row) > 0):
#             r = row

#     print(ShellSort(r))
