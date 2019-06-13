#Codigo para criar um CSV do tipo Source-Target-Weight
#Entrada: apoeapocnovo.csv
#Cada linha e um paciente
#0-176 pacientes controle, 177-248 doentes
#Coluna 1 alterada para inteiros de zero a N (248 entradas)
#cabecalho: id, sex, age, apoe.a1, apoe.a2, apoc.a1, apoc.a2, y

import csv
import numpy as np
from numpy import genfromtxt
import math


my_data = genfromtxt('apoeapocnovo.csv', delimiter=',')
#print len(my_data)
#print len(my_data[0])
e13 = 300
e12 = 301
e23 = 302
e22 = 303

c11 = 304
c12 = 305
c21 = 306
c22 = 307 
        

with open('saidaapoeapoc-new.csv', mode='w') as source1:
    source1_writer = csv.writer(source1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(my_data)):
        k = int(my_data[i][0])
        if my_data[i][3] == 3:
	    source1_writer.writerow([k, e13 ,1])
        if my_data[i][3] == 2:
	    source1_writer.writerow([k, e12,1])
        if my_data[i][4] == 3:
	    source1_writer.writerow([k, e23,1])
        if my_data[i][4] == 2:
	    source1_writer.writerow([k, e22,1])
        if my_data[i][5] == 1:
	    source1_writer.writerow([k, c11 ,1])
        if my_data[i][5] == 2:
	    source1_writer.writerow([k, c12,1])
        if my_data[i][6] == 1:
	    source1_writer.writerow([k, c21,1])
        if my_data[i][6] == 2:
	    source1_writer.writerow([k, c22,1])



















