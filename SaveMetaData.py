import os
import json
import pandas as pd

def SaveMetaData(where, metadata, name):
    file = './MetaData/'+where
    try:
        os.makedirs(file)
    except:
        print(file+' pasta já criada')

    with open(file+'/'+name, 'w') as f:
        f.write(json.dumps(metadata.__dict__))

def SaveMetaDataCSV(csvDir, metadata, columnName, row):
    print(row)
    csv = pd.read_csv(csvDir, index_col=0) 
    csv.loc[row, columnName] =  metadata.tempo #não importa o tipo
    csv.to_csv(csvDir)


class metadata:
    def __init__(self, trocas, tempo) -> None:
        self.trocas = trocas  # quantidade de trocas efetuadas
        self.tempo = tempo  # tempo em ms
