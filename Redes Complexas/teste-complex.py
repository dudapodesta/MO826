import pandas as pd
import numpy as np
import csv
from numpy import genfromtxt
import matplotlib
import matplotlib.pyplot as plt

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

#Teste para rede com 11 ou 12 atributos iguais
#Para rede com 10,11 ou 12 atributos iguais, use 
#source_target = source_target - 9
source_target = source_target - 10

#source_target se 0 fica 0, se >0 fica 1
B = np.where(source_target > 0.5, 1, 0)
vector = np.zeros(l)
vector = B.sum(axis=1)
#print vector
matplotlib.pyplot.hist(vector)
plt.show()
vector = vector - 1
#print vector
matplotlib.pyplot.hist(vector)
plt.show()
    

