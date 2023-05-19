import csv
import os
import pandas as pd
import time
import re
from SaveMetaData import SaveMetaDataCSV, metadata
import multiprocessing as mp

enderecos = ['./DATA/ordenado/asc', './DATA/ordenado/desc', './DATA/aleatorio']
metodos = ['BubbleSort', 'SelectionSort', 'InsertionSort','TimSort',
           'HeapSort', 'QuickSort', 'ShellSort', 'MergeSort']

# metodos = ['QuickSort']

tamanhos = [pow(10, 3), pow(10, 4), pow(10, 5), 2*pow(10, 5), 3*pow(10, 5), 4*pow(10, 5),
            5*pow(10, 5), 6*pow(10, 5), 7*pow(10, 5), 8*pow(10, 5), 9*pow(10, 5), pow(10, 6)]

ArquivosMetaDataTempo = {
    'Aleatorio': './MetaData/vetor_aleatorio_tempo_por_entrada.csv',
    'asc': './MetaData/vetor_ordenado_asc_tempo_por_entrada.csv',
    'desc': './MetaData/vetor_ordenado_desc_tempo_por_entrada.csv'
}

ArquivosMetaDataTroca = {
    'Aleatorio': './MetaData/vetor_aleatorio_trocas_por_entrada.csv',
    'asc': './MetaData/vetor_ordenado_asc_trocas_por_entrada.csv',
    'desc': './MetaData/vetor_ordenado_desc_trocas_por_entrada.csv'
}


class main:
    def __init__(self) -> None:
        data = self.ReadAllData()
        self.buildMetadata()
        # # chama função de outro arquivo ou classe
        # # tim = getattr(__import__('SelectionSort'), 'SelectionSort')

        # test = data[len(data)-4].name

        # print(re.sub('[^0-9]','', '51548545.csv'))
        # ret = self.RunMethod(metodos[5], data['Aleatorio'][3].data)
        # print(ret)
        # self.SaveData(
        # ArquivosMetaDataTempo['Aleatorio'], ret,  data['al'][3].name, metodos[3])

        for a in data:  # percorre as pastas asc des e aleatorio
            for v in data[a]:  # percorre os vetores tamanho
                print('Iniciando: ', a, v.name)
                for m in metodos:  # percorre os metodos
                    ret = self.RunMethod(m, v.data.copy())
                    self.SaveData(a, ret, v.name, m)
                print('Finalizado', a, v.name)

    def ReadAllMethods(self):
        pass

    def RunMethod(self, method, data):
        print(method)
        inicio = time.time()
        mt = getattr(__import__(method), method)
        print('Iniciando: ', method, 'tamanho: ', len(data))
        count = mt(data)
        fim = time.time()
        print('Finalizado: ', method, 'tempo: ', fim - inicio)
        return {
            'count': count,
            'tempo': (fim - inicio)
        }

    def SaveData(self, endereco, data, index: str, method):
        # print(index)
        meta = metadata(tempo=data['tempo'], trocas=data['count'])
        SaveMetaDataCSV(ArquivosMetaDataTempo[endereco], meta, method,
                        int(re.sub('[^0-9]', '', index)))

        meta.tempo = data['count']
        SaveMetaDataCSV(ArquivosMetaDataTroca[endereco], meta, method,
                        int(re.sub('[^0-9]', '', index)))

    # faz a leitura de todos os dados

    def ReadAllData(self):
        retorno = {
            "asc": [],
            "desc": [],
            "Aleatorio": []
        }

        for dir in enderecos:
            for file in os.listdir(dir):
                dt = None
                with open(dir+'/'+file, 'r') as f:
                    reader = csv.reader(f)
                    r = 0
                    for row in reader:
                        if (len(row) > 0):
                            r = row
                    dt = data(file, r, dir)

                if ('aleatorio' in dir):
                    retorno.get('Aleatorio').append(dt)
                else:
                    if ('asc' in dir):
                        retorno.get('asc').append(dt)
                    else:
                        retorno.get('desc').append(dt)
        return retorno

    def IsSorted(self, lista):
        is_sorted = all(a <= b for a, b in zip(lista, lista[1:]))

        # print the result
        if is_sorted:
            print("Yes, the list is sorted.")
        else:
            print("No, the list is not sorted.")

    # cria a tabela metadata com os headers e a primeira coluna
    def buildMetadata(self):
        data = {}
        zerado = []
        for i in tamanhos:
            zerado.append(0.00)

        for i in metodos:
            data[i] = zerado

        frame = pd.DataFrame(data=data, index=tamanhos)
        frame.index.name = 'Tam. Entrada'
        # por tempo
        frame.to_csv('./MetaData/vetor_aleatorio_tempo_por_entrada.csv')
        frame.to_csv('./MetaData/vetor_ordenado_asc_tempo_por_entrada.csv')
        frame.to_csv('./MetaData/vetor_ordenado_desc_tempo_por_entrada.csv')
        # por quantidade de trocas
        frame.to_csv('./MetaData/vetor_aleatorio_trocas_por_entrada.csv')
        frame.to_csv('./MetaData/vetor_ordenado_asc_trocas_por_entrada.csv')
        frame.to_csv('./MetaData/vetor_ordenado_desc_trocas_por_entrada.csv')


class data:
    def __init__(self, name, vector, dir) -> None:
        self.name = name
        self.data = vector
        self.dir = dir



process = mp.Process(target=main)

process.start()