import csv
import os

enderecos = ['./ordenado/asc', './ordenado/desc', './aleatorio']
methods = ['BubbleSort', 'SelectionSort',
           'InsertionSort', 'TimSort', 'HeapSort']


class main:
    def __init__(self) -> None:
        # data = self.ReadAllData()

        # # chama função de outro arquivo ou classe
        # # tim = getattr(__import__('SelectionSort'), 'SelectionSort')

        # test = data[len(data)-4].name

        # print(test)
        pass

    def ReadAllMethods(self):
        pass

    def RunMethod(self, method):
        pass

    # faz a leitura de todos os dados
    def ReadAllData(self):
        retorno = []
        for dir in enderecos:
            for file in os.listdir(dir):
                dt = None
                with open(dir+'/'+file, 'r') as f:
                    reader = csv.reader(f)
                    r = 0
                    for row in reader:
                        if (len(row) > 0):
                            r = row
                    dt = data(dir+'/'+file, r)

                retorno.append(dt)
        return retorno

    def IsSorted(self, lista):
        is_sorted = all(a <= b for a, b in zip(lista, lista[1:]))

        # print the result
        if is_sorted:
            print("Yes, the list is sorted.")
        else:
            print("No, the list is not sorted.")


class data:
    def __init__(self, name, vector) -> None:
        self.name = name
        self.data = vector


main()
