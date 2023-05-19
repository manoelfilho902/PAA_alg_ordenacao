import pandas as pd
import datetime, time

csvDir = './vetor_ordenado_asc_tempo_por_entrada.csv'

csv = pd.read_csv(csvDir, index_col=0)


for i in csv.index:
    for j in csv:
        # field = str(csv.loc[i, j]).replace('.', '')
        # print(field)
        # dt = datetime.datetime.fromtimestamp(field*1000)
        # if(field == 0):
        #     csv.loc[i, j] = '00:00:00.000';
        # else:
        #
             
        # csv.loc[i, j] = int(field);
        pd.to_datetime(csv.loc[i, j])

csv.to_csv(csvDir)
# print(time.time(), time.time_ns())