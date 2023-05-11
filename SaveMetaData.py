import os
import json

def SaveMetaData(where, metadata, name):
    file = './MetaData/'+where
    try:
        os.makedirs(file)
    except:
        print(file+' pasta já criada')

    with open(file+'/'+name, 'w') as f:
        f.write(json.dumps(metadata.__dict__))


class metadata:
    def __init__(self, trocas, tempo) -> None:
        self.trocas = trocas  # quantidade de trocas efetuadas
        self.tempo = tempo  # tempo em ms
