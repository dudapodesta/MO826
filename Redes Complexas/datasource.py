import pandas as pd
import numpy as np
import csv

#NACCID,NPSEX,NACCNEUR,NACCDIFF,NACCVASC,NACCAMY,
#NACCINF,NACCHEM,NACCARTE,NACCLEWY,NACCPRIO,NACCDOWN,NACCOTHP
alz = pd.read_csv('dataset-alz.csv')

for i in range(len(alz)):
    if alz['NACCNEUR'][i] == 9 or alz['NACCNEUR'][i] == 8:
        alz['NACCID'][i] = -999
    elif alz['NACCDIFF'][i] == 9 or alz['NACCDIFF'][i] == 8:
        alz['NACCID'][i] = -999
    elif alz['NACCVASC'][i] == 9 or alz['NACCVASC'][i] == 8:
        alz['NACCID'][i] = -999
    elif alz['NACCAMY'][i] == 9 or alz['NACCAMY'][i] == 8:
        alz['NACCID'][i] = -999
    elif alz['NACCINF'][i] == 9 or alz['NACCINF'][i] == 8:
        alz['NACCID'][i] = -999
    elif alz['NACCHEM'][i] == 9 or alz['NACCHEM'][i] == 8:
        alz['NACCID'][i] = -999
    elif alz['NACCARTE'][i] == 9 or alz['NACCARTE'][i] == 8:
        alz['NACCID'][i] = -999
    elif alz['NACCLEWY'][i] == 9 or alz['NACCLEWY'][i] == 8:
        alz['NACCID'][i] = -999
    elif alz['NACCPRIO'][i] == 9 or alz['NACCPRIO'][i] == 8:
        alz['NACCID'][i] = -999
    elif alz['NACCDOWN'][i] == 9 or alz['NACCDOWN'][i] == 8:
        alz['NACCID'][i] = -999
    elif alz['NACCOTHP'][i] == 9 or alz['NACCOTHP'][i] == 8:
        alz['NACCID'][i] = -999

with open('dataset-interm.csv', mode='w') as source1:
    source1_writer = csv.writer(source1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(alz)):
        if alz['NACCID'][i] > -1:
                source1_writer.writerow([alz['NACCID'][i], alz['NPSEX'][i], alz['NACCNEUR'][i], alz['NACCDIFF'][i], alz['NACCVASC'][i], alz['NACCAMY'][i], alz['NACCINF'][i], alz['NACCHEM'][i], alz['NACCARTE'][i], alz['NACCID'][i], alz['NACCLEWY'][i], alz['NACCPRIO'][i], alz['NACCDOWN'][i], alz['NACCOTHP'][i]])















