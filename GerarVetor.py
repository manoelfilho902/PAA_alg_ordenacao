import random
import csv
import os
from main import enderecos, tamanhos



for f in enderecos:
    try:
        os.makedirs(f)
    except:
        print('Diretorio: ' + f + ' já criado!')

for i in tamanhos:
    ord = []
    aleat = []
    for j in range(i):
        ord.append(j)
        aleat.append(random.randrange(i))

    # pd.array(ord).(enderecos[0]  +'/'+str(i)+'.csv')
    # pd.DataFrame(unord).to_csv(enderecos[1]+'/'+str(i)+'.csv')
    # pd.DataFrame(aleat).to_csv(enderecos[2]+'/'+str(i)+'.csv')

    with open(enderecos[0] + '/'+str(i)+'.csv', 'w', encoding='UTF-8') as f:
        w = csv.writer(f)
        w.writerow(ord)

    ord.reverse()
    with open(enderecos[1] + '/'+str(i)+'.csv', 'w', encoding='UTF-8') as f:
        w = csv.writer(f)
        w.writerow(ord)

    with open(enderecos[2] + '/'+str(i)+'.csv', 'w', encoding='UTF-8') as f:
        w = csv.writer(f)
        w.writerow(aleat)
