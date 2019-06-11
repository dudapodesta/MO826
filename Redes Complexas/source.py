#Codigo para criar um CSV do tipo Source-Target-Weight
#Entrada: NACC3.csv, dados alterados para termos apenas colunas sem campos vazios
#Cada linha e um paciente
#Coluna 1 alterada para inteiros de zero a N (5636 entradas)

import csv
import numpy as np
from numpy import genfromtxt


my_data = genfromtxt('NACC3.csv', delimiter=',')
#print len(my_data)
#print len(my_data[0])
#Matriz NxN para salvar valores dos pesos de uma aresta de Ni--Nj
#Matriz simetrica em relacao a diagonal principal
#source_target(i,j)=source_target(j,i)
l = len(my_data)
source_target = np.zeros((l,l))


for i in range(len(my_data)):
    for j in range(len(my_data)):
	k = int(my_data[i][0])
	n = int(my_data[j][0])
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
        if my_data[i][13] == my_data[j][13]:
	    source_target[k][n] = source_target[k][n]+1
        if my_data[i][14] == my_data[j][14]:
	    source_target[k][n] = source_target[k][n]+1

#Criar CSV's tipo Source-Target-Weight
#A partir de source_target, pegando apenas a parte triangular superior
#A diagonal principal nao nos interessa, nao quero aresta de No(i) para ele mesmo
#Montamos CSV com Source = i, Target = j, e Peso correspondente a posicao (i,j) em source_target
#Peso: 1,2,3...

with open('source_target4.csv', mode='w') as source1:
    source1_writer = csv.writer(source1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,len(source_target),1):
        for j in range(i+1,len(source_target[0]),1):
            if source_target[i][j]>4:
                source1_writer.writerow([i, j, source_target[i][j]-4])

with open('source_target5.csv', mode='w') as source2:
    source2_writer = csv.writer(source2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,len(source_target),1):
        for j in range(i+1,len(source_target[0]),1):
            if source_target[i][j]>5:
                source2_writer.writerow([i, j, source_target[i][j]-5])

with open('source_target6.csv', mode='w') as source3:
    source3_writer = csv.writer(source3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,len(source_target),1):
        for j in range(i+1,len(source_target[0]),1):
            if source_target[i][j]>6:
                source3_writer.writerow([i, j, source_target[i][j]-6])

with open('source_target7.csv', mode='w') as source5:
    source5_writer = csv.writer(source5, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,len(source_target),1):
        for j in range(i+1,len(source_target[0]),1):
            if source_target[i][j]>7:
                source5_writer.writerow([i, j, source_target[i][j]-7])
    















