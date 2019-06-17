import pandas as pd
import numpy as np
import csv
from numpy import genfromtxt

#NACCID,NPSEX,NACCNEUR,NACCDIFF,NACCVASC,NACCAMY,
#NACCINF,NACCHEM,NACCARTE,NACCLEWY,NACCPRIO,NACCDOWN,NACCOTHP
my_data = genfromtxt('dataset-interm.csv', delimiter=',')
#my_data = pd.read_csv('dataset-interm.csv', header=None )

l = len(my_data)
source_target = np.zeros((l,l))

for i in range(len(my_data)):
    for j in range(len(my_data)):
	k = int(my_data[i][0])
	n = int(my_data[j][0])
        if my_data[i][1] == my_data[j][1]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][2] == my_data[j][2]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][3] == my_data[j][3]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][4] == my_data[j][4]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][5] == my_data[j][5]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][6] == my_data[j][6]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][7] == my_data[j][7]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][8] == my_data[j][8]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][9] == my_data[j][9]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][10] == my_data[j][10]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][11] == my_data[j][11]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][12] == my_data[j][12]:
	    source_target[k][n] = source_target[k][n]+1

with open('dataset-saida1.csv', mode='w') as source3:
    source3_writer = csv.writer(source3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,len(source_target),1):
        for j in range(i+1,len(source_target[0]),1):
            if source_target[i][j]>10:
                source3_writer.writerow([i, j, source_target[i][j]-10])

with open('dataset-saida2.csv', mode='w') as source5:
    source5_writer = csv.writer(source5, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,len(source_target),1):
        for j in range(i+1,len(source_target[0]),1):
            if source_target[i][j]>8:
                source5_writer.writerow([i, j, source_target[i][j]-8])


