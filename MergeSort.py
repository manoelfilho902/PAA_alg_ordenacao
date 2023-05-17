from TimSort import Merge
import sys

def MergeSort(A):
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(A)+900))
    return MergeSortHelper(A, 0, len(A) - 1, 0)


def MergeSortHelper(A, left, rigth, count):
    
    if (left < rigth):
        meio = int((left + rigth) / 2)
        MergeSortHelper(A, left, meio, count)
        MergeSortHelper(A, meio +1, rigth, count)

        count += Merge(A, left, meio, rigth)

        return count


# import csv
# with open('./DATA/ordenado/desc/1000000.csv') as f:
#     reader = csv.reader(f)
#     r = 0
#     for row in reader:
#         if (len(row) > 0):
#             r = row
    
#     print(MergeSort(r))